# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

from frappe.utils import cstr
from frappe import msgprint, throw, _

from frappe.model.document import Document
from frappe.model.naming import parse_naming_series
from frappe.permissions import get_doctypes_with_read

from erpnext.setup.doctype.naming_series.naming_series import NamingSeries

def scrub_options_list(self, ol):
	serial_list  = filter(lambda x: x, [cstr(n).strip() for n in ol]) 
	liste = list(serial_list)
	return liste

@frappe.whitelist(allow_guest=False)                                              
def build_options(self):
	"""update series list"""
	NamingSeries.scrub_options_list = scrub_options_list

#	frappe.throw(options)