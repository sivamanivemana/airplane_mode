// Copyright (c) 2024, Mohan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tenant Contract", {
    onload:function(frm){
        frappe.db.get_value("Global Configuration", "Global Configuration",["default_rent_amount", "rent_amount"],(g)=>{
            if(g.default_rent_amount && !frm.doc.amount){
                frm.set_value("amount", g.rent_amount)
            }
        })
    },
	payment_due_date_of_every_month(frm) {
        frm.call({
			method: "get_due_date",
			args: {payment_due_day:frm.doc.payment_due_date_of_every_month}
		}).then((r) => {
			if (r.message) {
				frm.set_value("payment_due_date", r.message)
			}
		});
	},
});
