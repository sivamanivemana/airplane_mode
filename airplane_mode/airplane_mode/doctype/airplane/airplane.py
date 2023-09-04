# Copyright (c) 2023, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):

    @frappe.whitelist()
    def user_role(self):

        user = frappe.get_roles(frappe.session.user)
        
        if not "Airport Authority Personnel" in user:
            return False

        else:
            return True


		# cur_frm.layout.primary_button.css('color', 'black')

		# cur_frm.layout.primary_button.removeClass("btn-primary")

		# cur_frm.layout.primary_button.addClass("btn-secondary")

		# cur_frm.fields.at(7).input_area.firstChild.children[1].remove()