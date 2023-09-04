// Copyright (c) 2023, Rohit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane', {
	refresh: function(frm) {

		frm.call('user_role')
		.then((r) => {
			console.log(r)
			if (r.message == false){
				cur_frm.set_df_property("initial_audit_completed", "hidden", 1);
			}
		});

		cur_frm.attachments.parent.css('display','none');

		cur_frm.sidebar.page.sidebar.css('display','none');

		this.cur_frm.parent.firstChild.querySelector(".dropdown-menu-right").childNodes[7].remove()

		// cur_frm.fields.at(7).input_area.firstChild.children[1].remove()

		// cur_frm.layout.primary_button.css('color', 'black')

		// cur_frm.layout.primary_button.removeClass("btn-primary")

		// cur_frm.layout.primary_button.addClass("btn-secondary")

	}
});
