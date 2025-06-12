# Copyright (c) 2025, YASH GAUTAM and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Flightpassenger(Document):
	

	def before_save(self):

		self.full_name= self.first_name + " " + self.last

	

