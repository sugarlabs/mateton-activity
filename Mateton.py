#      MATETON - Un pizarron para los ninos
#  Copyright (C) 2011 - Rodrigo Perez Fulloni
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


from Control import Control
from sugar.activity import activity
import simplejson

import pygtk
pygtk.require('2.0')
import gtk

from time import gmtime, strftime

__author__ = "rodripf"
__date__ = "$12/05/2011 08:21:57 AM$"

class Mateton(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        toolbox = activity.ActivityToolbox(self)

        activity_toolbar = toolbox.get_activity_toolbar()
        activity_toolbar.share.props.visible = False #Todavia no hay share
        activity_toolbar.show()

        self.set_toolbox(toolbox)
        toolbox.show()

        self.activity = Control()

        self.set_canvas(self.activity.todo)
        self.nomArch =""


    def read_file(self, file_path):
        if self.metadata['mime_type'] != 'text/plain':
            return

        fd = open(file_path, 'r')
        text = fd.read()
        data = simplejson.loads(text)
        fd.close()
        self.nomArch = data['name']
        self.activity.cargar(nombre = self.nomArch)
        print "cargo"

    def write_file(self, file_path):
        if not self.metadata['mime_type']:
            self.metadata['mime_type'] = 'text/plain'

        data = {}
        if self.nomArch =="":
            data['name'] = strftime("%d-%b-%Y-%H:%M:%S", gmtime())
        else:
            data['name'] = self.nomArch

        fd = open(file_path, 'w')
        text = simplejson.dumps(data)
        fd.write(text)
        fd.close()

        self.activity.mantener(nombre = data['name'])
        print "salvo"