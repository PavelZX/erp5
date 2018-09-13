#!/usr/bin/python
##############################################################################
#
# Copyright (c) 2009 Nexedi SA and Contributors. All Rights Reserved.
#                    Vincent Pelletier <vincent@nexedi.com>
#                    Sebastien Robin <seb@nexedi.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
from __future__ import print_function

from datetime import date
from os import path
import rpy2.robjects as robjects
import os
from optparse import OptionParser
r = robjects.r

usage = """
  Usage:
    %prog [OPTION] file1.csv [file2.csv [...]]
  Result:
    Generates, in current directory, a graph per csv column in out-type format.
    Their name is composed of:
    - csv file basename (without extension)
    - csv column title
    - the ratio of present points (100 to 000). The higher the number, the
      more the plot will be complete (less holes, longer timespan coverage).
    - out-type extension

  CSV files must have been generated by parse_timing_log.py tool.
"""

class CSVFile(object):
  def __init__(self, file_name, field_delim=','):
    file = open(file_name, 'r')
    self.column_dict = column_dict = {}
    self.column_list = column_list = []
    self.ratio_dict = ratio_dict = {}
    line_num = 0
    self.value_max = value_max = {}
    next_ord = 0
    for x, title in enumerate(file.readline().split(field_delim)):
      title = title.strip()
      title = title.strip('"')
      if title in column_dict:
        title = next_ord
        while title in column_dict:
          title += 1
        next_ord = title + 1
        title = str(title)
      column_dict[title] = []
      column_list.append(title)
    for line in file.readlines():
      line_num += 1
      for x, cell in enumerate(line.split(field_delim)):
        cell = cell.strip()
        key = column_list[x]
        if x != 0:
          cell = computeExpr(cell)
          if cell is not None:
            ratio = ratio_dict.get(key, 0)
            ratio_dict[key] = ratio + 1
            if cell > value_max.get(key, 0):
              value_max[key] = cell
        column_dict[key].append(cell)
    line_num = float(line_num) / 100
    for key in ratio_dict:
      ratio_dict[key] /= line_num

  def getColumn(self, column_id):
    return self.column_dict[self.column_list[column_id]]

  def iterColumns(self, start=0, stop=None):
    if stop is None:
      column_list = self.column_list[start:]
    else:
      column_list = self.column_list[start:stop]
    return ((x, self.column_dict[x], self.value_max.get(x, 0), self.ratio_dict.get(x, 0)) for x in column_list)

def computeExpr(expr):
  # only supports '=x/y'
  if expr:
    assert expr[0] == '='
    num, denom = expr[1:].split('/')
    result = float(int(num)) / int(denom)
  else:
    result = None
  return result

def main():
  parser = OptionParser(usage)
  parser.add_option("--with-regression", action="store_true",
    dest="regression_enabled", help="enable B-spline regression")
  parser.add_option("--ignored-quantity", type="int", dest="ignored_quantity",
    help="ignore IGNORED_QUANTITY higher values that might make a graph totally unusable")
  parser.add_option("--out-type", type="string", default="png",
    help="can be %default (default) or svg")
  parser.add_option("--minimal-non-empty-values-ratio", type="float",
    dest="minimal_non_empty_ratio", default=None,
    help="graph with ratio of non empty values with lesser than value, then graph is ignored")
  (options, file_name_list) = parser.parse_args()

  current_dir = os.getcwd()
  for file_name in file_name_list:
    print('Loading %s...' % (file_name, ))
    file = CSVFile(file_name)

    date_string_list = file.getColumn(0)
    date_list = []
    x_label_value_list = []
    # plotting functionnalities does not select smartly
    # a good number of x values to display, so we will display 20 dates
    # in order to have good enough dates on the x axis.
    # x_label_value_list will be like [1, 5, 10...]
    # date_list will be like ['2009/07/01', '2009/07/05', '2009/07/10', ...]
    factor = 1
    if len(date_string_list) > 20:
      factor = int(len(date_string_list) / 20)
    i = 0
    for date_string in date_string_list:
      if i % factor == 0:
        x_label_value_list.append(i)
        date_split = date_string.replace('"','').split('/')
        date_split.reverse()
        new_date = '/'.join(date_split)
        date_list.append(new_date)
      i += 1
    max_x = len(date_string_list)
    # knots are used for B-spline regression
    # We need to add three additional knots at the begin and end in
    # order to have the right basis
    knot_list  = [x_label_value_list[0]] * 3 + x_label_value_list \
        + [max_x] * 4
    r_x_label_value_list = robjects.FloatVector(x_label_value_list)
    robjects.globalenv["x_label_value_list"] = r_x_label_value_list
    robjects.globalenv["knot_list"] = knot_list
    r("x_label <- c(%s)" % ','.join(['"%s"' % x for x in date_list]))
    # import the splines library in R
    if options.regression_enabled:
      r("library(splines)")
    # now parse all columns and store a out-type file
    for title, column, value_max, ratio in file.iterColumns(start=1):
      out_file, out_ext = path.splitext(path.basename(file_name))
      if out_ext != '.csv':
        out_file = '.'.join((out_file, out_ext))
      out_file_name = '%s_%s_%03i.%s' % (out_file, title.replace('%',''),
          ratio, options.out_type)
      i = 0
      x_data = []
      y_data = []
      # First parse the list to retrieve values that we might want to remove
      ignored_value_set = set([])
      max_y_data = []
      if options.ignored_quantity not in (None, 0):
        for value in column:
          if value is not None:
            max_y_data.append(value)
        max_y_data.sort()
        ignored_value_set = set(max_y_data[-options.ignored_quantity:])
      # build list with all data that we want to display
      for value in column:
        if value is not None and not (value in ignored_value_set):
          x_data.append(i)
          y_data.append(value)
        i += 1
      if len(x_data) == 0:
        print('Nothing to plot for %s...' % (out_file_name, ))
        continue
      if options.minimal_non_empty_ratio is not None:
        column_len = len(column)
        if column_len:
          if float(len(x_data))/column_len < options.minimal_non_empty_ratio:
            print('Not enough values to plot for %s...' % (out_file_name, ))
            continue
      r_y_data = robjects.FloatVector(y_data)
      r_x_data = robjects.FloatVector(x_data)
      robjects.globalenv["y_data"] = r_y_data
      robjects.globalenv["x_data"] = r_x_data
      display_column_regression = options.regression_enabled
      # if there is no more than one unique point, regression is useless
      if len(set([x for x in r_y_data])) <= 1:
        display_column_regression = 0
      regression_string = ''
      # Calculate a B-spline regression in order to give clear overview
      # about the direction of chaotics values.
      if display_column_regression:
        r("bx <- splineDesign(knot_list, x_data)")
        r("fitted_model <- lm(y_data ~ bx)")
        regression_string = ', fitted_model$fit'
      # Define the place where to store the graphe and format of the image
      r("""%s(file='%s/%s', width=800, height=600)""" % (options.out_type,
        current_dir, out_file_name))
      # Increase the size for the place of the bottom axis labels (x)
      r("""par(mar=c(9, 4, 4, 2) + 0.1)""")
      # Plot the graph itself
      r("""matplot(x_data, cbind(y_data %s), type='ll',
                lty=1, main='%s (average display time per day)',
                xlab='', ylab='time (s)', xaxt='n')""" % (
                  regression_string, title))
      r("""axis(1, at=x_label_value_list, lab=x_label, las=2)""")
      # stop changing the out-type file
      r("""dev.off()""")

      print('Saving %s...' % (out_file_name, ))

if __name__ == '__main__':
  main()

