# Copyright (c) 2025, YASH GAUTAM and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from airplane_mode.airplane_mode.utils import create_random 


class AirplaneTicket(Document):
	

	def validate(self):
		self.remove_duplicate_add_ons()


	def before_save(self):
		self.calculate_total_price()
		self.seat=create_random()


	def before_submit(self):
		self.check_status()



	def check_status(self):
		if self.status != "Boarded":
			frappe.throw("Please go through the boarding process")


	def remove_duplicate_add_ons(self):
		seen=set()

		for item in self.add_ons:
			if item.item in seen:
				frappe.throw(f"{item.item} cannot be added more than one time . Please Increase Quantity")
			else:
				seen.add(item.item)
		print(seen)
	
	def calculate_total_price(self):

		total=0

		for item in self.add_ons:
			total+= (item.amount * item.quantity)

		self.total_price=total + self.flight_price
