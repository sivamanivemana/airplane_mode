// Copyright (c) 2023, Rohit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane', {
	refresh: function(frm) {

		frappe.call({

			method: "airplane_mode.airplane_mode.doctype.airplane.airplane.user_role",
			
		
		}).then((r) => {
			if (r.message == false){
				cur_frm.set_df_property("initial_audit_completed", "hidden", 1);
			}
		})

	}
});
