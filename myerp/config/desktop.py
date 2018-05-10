# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
           {
               "module_name": "Myerp",          
               "color": "grey",
               "icon": "octicon octicon-repo",
               "type": "module",
               "label": _("Myerp")
           },
           {
	       "module_name": "Compta",
               "color": "grey",
               "icon": "octicon octicon-repo",
               "type": "module",
               "label": _("Compta")
           }
        ]         
