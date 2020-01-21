#      MATETON - Un pizarron para los ninos
#  Copyright (C) 2011 - 2013 Rodrigo Perez Fulloni
#Departamento de Ingenieria, Fundacion Teleton
#             Montevideo, Uruguay
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from sugar3.activity.widgets import StopButton, ShareButton, DescriptionItem, TitleEntry, ActivityButton
from sugar3.graphics.toolbarbox import ToolbarBox

from Control import Control
from sugar3.activity import activity
import simplejson
import sugar3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from time import gmtime, strftime

__author__ = "rodripf"
__date__ = "$12/05/2011 08:21:57 AM$"

class Mateton(activity.Activity):
    _NEW_TOOLBAR_SUPPORT = True
    try:
        from sugar3.graphics.toolbarbox import ToolbarBox
        from sugar3.graphics.toolbarbox import ToolbarButton
        from sugar3.activity.widgets import StopButton
        from sugar3.activity.widgets import ActivityToolbar
    except:
        _NEW_TOOLBAR_SUPPORT = False


    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.build_toolbar()
        self.activity = Control()

        self.set_canvas(self.activity.todo)
        self.nomArch =""
        
        self.connect('key_press_event', self.activity.onKeyPress)

    def build_toolbar(self):

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def read_file(self, file_path):
        if self.metadata['mime_type'] != 'text/plain':
            return

        fd = open(file_path, 'r')
        text = fd.read()
        data = simplejson.loads(text)
        fd.close()
        self.nomArch = data['name']
        self.activity.cargar(nombre = self.nomArch)

    def write_file(self, file_path):
        if not self.metadata['mime_type']:
            self.metadata['mime_type'] = 'text/plain'

        data = {}
        if self.nomArch =="":
            data['name'] = strftime("%d%b%Y%H%M%S", gmtime())
        else:
            data['name'] = self.nomArch

        fd = open(file_path, 'w')
        text = simplejson.dumps(data)
        fd.write(text)
        fd.close()

        self.activity.mantener(nombre = data['name'])

