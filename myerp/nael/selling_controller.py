# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.utils import flt, cint, add_days, cstr, add_months
import json, ast

from erpnext.controllers.selling_controller import SellingController

from six import string_types, iteritems

@frappe.whitelist(allow_guest=False) 
def validate(self):
	super(SellingController, self).validate()
	self.validate_max_discount()
	self.validate_selling_price()
	self.set_qty_as_per_stock_uom()
	self.set_po_nos()
#	dic_m = ast.literal_eval(doc_m)
#	dic = frappe._dict(dic_m)
#	dic = json.loads(doc_m)  
	check_active_sales_items(self)              

@frappe.whitelist(allow_guest=False)                                              
def build_items(self):
	"""update series list"""
	SellingController.validate = validate


def check_active_sales_items(obj):
	for d in obj.get("items"):
		if d.item_code:
			item = frappe.db.sql("""select i.docstatus, id.income_account
				from `tabItem` i, `tabItem Default` id
				where i.name=%s and id.parent=i.name and id.company=%s""",
				(d.item_code, obj.company), as_dict=True)

			if getattr(d, "income_account", None):
				doc = frappe.get_doc("Item", d.item_code)
				if item:
#					frappe.throw("je suis ici178")
					for default in doc.item_defaults:
						if default.company == obj.company:
							cat_cpt = frappe.db.get_value("Customer", obj.customer, "categorie_comptable")
							if cat_cpt == "Cession":
								default.default_cession_account = d.income_account	
							else:
								default.income_account = d.income_account						
							break
				elif not item:
					doc.append("item_defaults", {
						"company": obj.company,
						"income_account": d.income_account,
					})
				doc.save()
