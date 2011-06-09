from Control import Control
from sugar.activity import activity
import simplejson

import pygtk
pygtk.require('2.0')
import gtk

from time import gmtime, strftime
from sugar.graphics.toolbutton import ToolButton
from gettext import gettext as _

__author__ = "rodripf"
__date__ = "$12/05/2011 08:21:57 AM$"

class Mateton(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        toolbox = activity.ActivityToolbox(self)

        activity_toolbar = toolbox.get_activity_toolbar()
        activity_toolbar.share.props.visible = False #Todavia no hay share
        activity_toolbar.show()

        self.acerca_bt = ToolButton('acerca')
        self.acerca_bt.set_tooltip(_('Acerca de...'))
        activity_toolbar.insert(self.acerca_bt, -1)
	self.acerca_bt.connect('clicked', self.acerca)
	self.acerca_bt.show()

        self.set_toolbox(toolbox)
        toolbox.show()

        self.activity = Control()

        self.set_canvas(self.activity.todo)


    def read_file(self, file_path):
        if self.metadata['mime_type'] != 'text/plain':
            return

        fd = open(file_path, 'r')
        text = fd.read()
        data = simplejson.loads(text)
        fd.close()

        self.activity.cargar(nombre = data['name'])
        pass

    def write_file(self, file_path):
        if not self.metadata['mime_type']:
            self.metadata['mime_type'] = 'text/plain'

        data = {}
        data['name'] = strftime("%d-%b-%Y-%H:%M:%S", gmtime())

        fd = open(file_path, 'w')
        text = simplejson.dumps(data)
        fd.write(text)
        fd.close()

        self.activity.mantener(nombre = data['name'])
        pass


    def acerca(self, data):
        print "Hola"
        about = gtk.AboutDialog()
        about.set_program_name("Mateton")
        about.set_version("2.0")
        about.set_copyright(_("Rodrigo Perez Fulloni - Released under the GPL v.3.0"))
        about.set_comments(_("Departamento de Inenieria - Fundacion Teleton\nMontevideo Uruguay"))
        about.set_website("http://www.teleton.org.uy")
        about.set_logo(gtk.gdk.pixbuf_new_from_file("activity/teleton.gif"))
        about.run()
        about.destroy()
        pass


