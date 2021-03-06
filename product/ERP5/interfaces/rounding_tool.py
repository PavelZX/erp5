# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 Nexedi KK and Contributors. All Rights Reserved.
#                    Yusei Tahara <yusei@nexedi.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract a Free Software
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

from zope.interface import Interface

class IRoundingTool(Interface):
  """
  Rounding tool interface
  """

  def findRoundingModelValueList(document, property_id=None, context=None):
    """
    Find matched rounding models for context and property id.

    Parameters:

    document
      This is the object which contains value to be rounded.

    property_id
      XXX I'm not quite sure if this is really necessary or not...
      This indicates which property value is rounded.

    context
      This indicates where lookup starts from. If this is None, then rounding
      tool itself is used.

    Example:

      temporary_movement is generated by getAggregatedAmountList from a set of
      movements and represents total price with tax. trade_model_line contains
      a rounding model to be used here to round the total price with tax.

      portal_roundings.findRoundingModel(temporary_movement, 'total_price',
                                         context=trade_model_line)
    """

  def getRoundingProxy(document, context=None):
    """
    Find matched rounding models from context and return proxy object for
    `document`. The proxy object returns rounded value through getters.
    """
