# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "myerp"
app_title = "Myerp"
app_publisher = "R.K"
app_description = "Myerp"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "krahmoune@groupefa.com"
app_license = "MIT"

                                                                                              
doc_events = {
#	"Sales Invoice": {
#		"validate": "myerp.nael.selling_controller.validate"
#	}
}

doctype_js = {
#	"Fiscal Year": ["erpnext_france/custom_scripts/fiscal_year.js"],
#	"Payment Entry": ["erpnext_france/custom_scripts/payment_entry.js"],
#	"Journal Entry": ["myerp/custom_scripts/journal_entry.js"],
	"Naming Series": ["myerp/custom_scripts/series.js"],
	"Sales Invoice": ["myerp/custom_scripts/selling_controller.js"]
}

#fixtures = [
#      {"dt": "Custom Field", "filters": [["name", "in", ["Salary Structure Employee-hs1"]]]}
#]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/myerp/css/myerp.css"
# app_include_js = "/assets/myerp/js/myerp.js"

# include js, css files in header of web template
# web_include_css = "/assets/myerp/css/myerp.css"
# web_include_js = "/assets/myerp/js/myerp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "myerp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "myerp.install.before_install"
# after_install = "myerp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "myerp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"myerp.tasks.all"
# 	],
# 	"daily": [
# 		"myerp.tasks.daily"
# 	],
# 	"hourly": [
# 		"myerp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"myerp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"myerp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "myerp.install.before_tests"

# Overriding Whitelisted Methods                     
# ------------------------------
#

override_whitelisted_methods = {
	"erpnext.stock.get_item_details.get_item_details": "myerp.nael.get_item_details.get_item_details"
#	"erpnext.controllers.selling_controller.check_active_sales_items": "myerp.nael.selling_controller.check_active_sales_items"
	}
#	"frappe.desk.naming_series.scrub_options_list": "myerp.fec.series.scrub_options_list"


