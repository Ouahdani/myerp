// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt


frappe.ui.form.on("Naming Series", "update", function(frm,cdt,cdn) {

//    frappe.msgprint(frm.doc);

    frappe.call({
        method: "myerp.nael.series.build_options",
		args: {
            self: frm.doc.set_options
        },
        callback: function(r) {
        }
    });
//	frappe.msgprint(frm.doc.set_options);
});