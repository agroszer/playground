import re
import os
import zope.component
import zope.event
import zope.interface
import zope.lifecycleevent
from z3c.form import button, field
from z3c.form.browser import textlines
from z3c.formui import form
from zope.error.interfaces import IErrorReportingUtility
from zope.publisher.interfaces import NotFound
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.publisher.skinnable import applySkin
from zope.traversing.interfaces import IContainmentRoot
from zope.traversing.browser.absoluteurl import absoluteURL


class ListPage(form.Form):
    ignoreContext = True

    @button.buttonAndHandler(u'Delete', name='delete')
    def handleDelete(self, action):
        self.status = u'Stuff deleted.'
