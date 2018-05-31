// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt


frappe.ui.form.on("Item", "item_group", function(frm,cdt,cdn) {

//    frappe.msgprint(frm.doc);

    frappe.call({
        method: "myerp.nael.item.update_defaults",
		args: {
            name: frm.doc.name,
			group: frm.doc.item_group
        },
        callback: function(r) {
        }
    });
//	frappe.msgprint(frm.doc.set_options);
});
