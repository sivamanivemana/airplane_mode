# Copyright (c) 2023, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
    pass


@frappe.whitelist()
def user_role():

    user = frappe.get_roles(frappe.session.user)

    if not "Airport Authority Personnel" in user:
        return False

    else:
        return True
