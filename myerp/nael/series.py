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

def get_current(self, arg=None):
	"""get series current"""
	if self.prefix:
		prefix = self.parse_naming_series()
		self.current_value = frappe.db.get_value("Series",
		prefix, "current", order_by = "name")
		self.code_journal = frappe.db.get_value("Series",
		prefix, "code_jour", order_by = "name")		
	
def update_series_start(self):
	if self.prefix:
		prefix = self.parse_naming_series()
		self.insert_series(prefix)
		frappe.db.sql("update `tabSeries` set current = %s where name = %s",
			(self.current_value, prefix))
		frappe.db.sql("update `tabSeries` set code_jour = %s where name = %s",
			(self.code_journal, prefix))			
		msgprint(_("Series Updated Successfully"))
	else:
		msgprint(_("Please select prefix first"))	

@frappe.whitelist(allow_guest=False)                                              
def build_options(self):
	"""update series list"""
	NamingSeries.scrub_options_list = scrub_options_list
	
@frappe.whitelist(allow_guest=False)                                              
def build_code_journal(self):
	"""update series list"""
	NamingSeries.get_current = get_current
	NamingSeries.update_series_start = update_series_start

	