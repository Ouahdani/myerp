# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe

from erpnext.stock.doctype.item.item import Item


def on_update(self, arg=None):
	item_default = frappe.db.get_value("Item Default", {"parent": self.name}, "name")
	inc_account = frappe.db.get_value("Item Default", {"name": item_default}, "income_account")
	if not inc_account:
		income_account = frappe.db.get_value("Item Group", {"name": self.item_group}, "default_income_account", order_by="name")
		frappe.db.set_value("Item Default", item_default , "income_account", income_account)
		self.reload()
	
	exp_account = frappe.db.get_value("Item Default", {"parent": self.name, "company": frappe.defaults.get_defaults().company}, "expense_account")
	if not exp_account:
		expense_account = frappe.db.get_value("Item Group", {"name": self.item_group}, "default_expense_account", order_by="name")
		frappe.db.set_value("Item Default", item_default , "expense_account", expense_account)
		self.reload()
	
@frappe.whitelist(allow_guest=False)  		
def update_defaults(name, group):
	item_default = frappe.db.get_value("Item Default", {"parent": name}, "name")
	inc_account = ""
	frappe.db.set_value("Item Default", item_default , "income_account", inc_account)-




