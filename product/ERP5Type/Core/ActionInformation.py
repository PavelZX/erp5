##############################################################################
#
# Copyright (c) 2002-2009 Nexedi SARL and Contributors. All Rights Reserved.
#                         Jean-Paul Smets <jp@nexedi.com>
#                         Ivan Tyagov <ivan@nerpix.com>
#                         Julien Muchembled <jm@nexedi.com>
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

import zope.interface
from AccessControl import ClassSecurityInfo, getSecurityManager
from Acquisition import aq_base
from Products.CMFCore.Expression import Expression
from Products.ERP5Type import interfaces, Constraint, Permissions, PropertySheet
from Products.ERP5Type.Permissions import AccessContentsInformation
from Products.ERP5Type.XMLObject import XMLObject


class ActionInformation(XMLObject):
  """
  ActionInformation is an ERP5 type which will eventually replace respective ActionInformation from CMF.
  """
  meta_type = 'ERP5 Action Information'
  portal_type = 'Action Information'
  add_permission = Permissions.AddPortalContent
  isPortalContent = 1
  isRADContent = 1
  icon = None # Override DynamicType.icon from CMFCore

  # Declarative security
  security = ClassSecurityInfo()
  security.declareObjectProtected(AccessContentsInformation)

  zope.interface.implements(interfaces.IAction)

  # Declarative properties
  property_sheets = ( PropertySheet.CategoryCore
                    , PropertySheet.DublinCore
                    , PropertySheet.ActionInformation
                    )

  security.declareProtected(AccessContentsInformation, 'test')
  def test(self, ec):
    """Test if the action should be displayed or not for the given context"""
    if self.isVisible():
      permission_list = self.getActionPermissionList()
      if permission_list:
        category = self.getActionType() or ''
        info = ec.vars
        if (info['here'] is not None and
            (category[:6] == 'object' or
             category[:8] == 'workflow')):
          context = info['here']
        elif (info['folder'] is not None and
              category[:6] == 'folder'):
          context = info['folder']
        else:
          context = info['portal']
        has_permission = getSecurityManager().getUser().has_permission
        for permission in permission_list:
          if not has_permission(permission, context):
            return False
      condition = self.getCondition()
      return condition is None or condition(ec)
    return False

  security.declareProtected(AccessContentsInformation, 'getActionInfo')
  def getActionInfo(self, ec):
    """Return a dict with values required to display the action"""
    action = self.getAction()
    icon = self.getIcon()
    return {'id': self.getReference(),
            'name': self.getTitle(),
            'description': self.getDescription(),
            'category':  self.getActionType(),
            'priority': self.getFloatIndex(),
            'icon': icon is not None and icon(ec) or '',
            'url': action is not None and action(ec) or '',
            }

  def _setAction(self, value):
    """Overridden setter for 'action' to accept strings and clean null values
    """
    if isinstance(value, basestring):
      value = value and Expression(value) or None
    self._baseSetAction(value)

  def _setCondition(self, value):
    """Overridden setter for 'condition' to accept string and clean null values
    """
    if isinstance(value, basestring):
      value = value and Expression(value) or None
    self._baseSetCondition(value)

  def _setIcon(self, value):
    """Overridden setter for 'icon' to accept string and clean null values
    """
    if isinstance(value, basestring):
      value = value and Expression(value) or None
    self._baseSetIcon(value)

  # XXX Following getAction/getCondition/getIcon are problably not useful
  #     because properties should already be cleaned up during migration
  #     or installation from BT.
  def getAction(self):
    """Overridden getter for 'action' to clean null values"""
    if getattr(aq_base(self), 'action', None) == '':
      del self.action
    return self._baseGetAction()

  def getCondition(self):
    """Overridden getter for 'condition' to clean null values"""
    if getattr(aq_base(self), 'condition', None) == '':
      del self.condition
    return self._baseGetCondition()

  def getIcon(self):
    """Overridden getter for 'icon' to clean null values"""
    if getattr(aq_base(self), 'icon', None) == '':
      del self.icon
    return self._baseGetIcon()

  security.declareProtected(AccessContentsInformation, 'getActionText')
  def getActionText(self):
    """Return the text of the action expression"""
    return getattr(self.getAction(), 'text', None)

  security.declareProtected(AccessContentsInformation, 'getConditionText')
  def getConditionText(self):
    """Return the text of the condition expression"""
    return getattr(self.getCondition(), 'text', None)

  security.declareProtected(AccessContentsInformation, 'getIconText')
  def getIconText(self):
    """Return the text of the icon expression"""
    return getattr(self.getIcon(), 'text', None)

  security.declareProtected(AccessContentsInformation, 'PrincipiaSearchSource')
  def PrincipiaSearchSource(self):
    """Return keywords for "Find" tab in ZMI"""
    search_source_list = [self.getReference(),
                          self.getTitle(),
                          self.getDescription(),
                          self.getActionText(),
                          self.getConditionText()]
    return ' '.join(filter(None, search_source_list))

  security.declareProtected(AccessContentsInformation, 'getActionType')
  def getActionType(self):
    # Since we should have only one category that starts with
    # 'action_type/' here, we call self.categories[0][12:] (12 is the
    # length of 'action_type/'), instead of self.getActionType() for
    # better performance.
    categories = getattr(self, 'categories', [])
    return len(categories) and categories[0][12:] or None

  security.declarePrivate('getRawActionInformation')
  def getRawActionInformation(self):
    """Return RawActionInformation instance that is not persistent and
    is cacheable."""
    # we cache cloned Expressions because original ones are persistent
    # objects.
    icon = self.getIcon()
    if icon is not None:
      icon = Expression(icon.text)
    action = self.getAction()
    if action is not None:
      action = Expression(action.text)
    condition = self.getCondition()
    if condition is not None:
      condition = Expression(condition.text)
    return RawActionInformation(
      {'id':self.getReference(),
       'name':self.getTitle(),
       'description':self.getDescription(),
       'category':self.getActionType(),
       'priority':self.getFloatIndex(),
       'icon':icon,
       'action':action,
       'condition':condition,
       'action_permission':self.getActionPermissionList(),
       }
      )

class RawActionInformation(object):
  """The purpose of this class is to provide a cacheable instance having
  an enough information of Action Information document."""

  def __init__(self, kw):
    self.action = kw.pop('action')
    self.icon = kw.pop('icon')
    self.condition = kw.pop('condition')
    self.action_permission = kw.pop('action_permission')
    self.param_dict = kw

  def getPriority(self):
    return self.param_dict['priority']

  def test(self, ec):
    """Test if the action should be displayed or not for the given context"""
    permission_list = self.action_permission
    if permission_list:
      category = self.param_dict['category'] or ''
      info = ec.vars
      if (info['here'] is not None and
          (category[:6] == 'object' or
           category[:8] == 'workflow')):
        context = info['here']
      elif (info['folder'] is not None and
            category[:6] == 'folder'):
        context = info['folder']
      else:
        context = info['portal']
      has_permission = getSecurityManager().getUser().has_permission
      for permission in permission_list:
        if not has_permission(permission, context):
          return False
    condition = self.condition
    return condition is None or condition(ec)

  def cook(self, ec):
    param_dict = self.param_dict.copy()
    action = self.action
    param_dict['url'] = action is not None and action(ec) or ''
    icon = self.icon
    param_dict['icon'] = icon is not None and icon(ec) or ''
    return param_dict
