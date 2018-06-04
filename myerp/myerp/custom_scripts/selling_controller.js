// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt


frappe.ui.form.on("Sales Invoice", "validate", function(frm, cdt, cdn) {

//	frappe.msgprint(frm.doc);
//	var jsonObject =  JSON.parse(frm.doc)
//	frappe.msgprint(jsonObject)
	
    frappe.call({
        method: "myerp.nael.selling_controller.build_items",
		args: {
			self: frm.doc.name
        },
        callback: function(r) {
        }
    });
//	frappe.msgprint(frm.doc.set_options);
});
