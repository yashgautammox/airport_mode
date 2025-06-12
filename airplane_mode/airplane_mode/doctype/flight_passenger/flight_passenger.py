# Copyright (c) 2025, YASH GAUTAM and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Flightpassenger(Document):
	

	def before_save(self):

		self.full_name= self.first_name + " " + self.last

	def validate(self):
		self.remove_duplicate_add_ons()


	def remove_duplicate_add_ons(self):
		seen=set()

		for item in self.add_ons:
			if item.name in seen:
				frappe.alert("This Add on Can Not be added more Than one Time")
			else:
				seen.add(item.name)
		print(seen)

