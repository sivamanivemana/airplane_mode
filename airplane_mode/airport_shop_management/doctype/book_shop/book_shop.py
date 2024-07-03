# Copyright (c) 2024, Mohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookShop(Document):
    def before_save(self):
        frappe.db.set_value("Shop", self.shop, "status", "Occupied")
