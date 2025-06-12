# Copyright (c) 2025, YASH GAUTAM and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from airplane_mode.airplane_mode.utils import create_random 


class AirplaneTicket(Document):
	

	def validate(self):
		self.remove_duplicate_add_ons()
		self.check_capacity()


	def before_save(self):
		self.calculate_total_price()
	


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

		try:
			flight_price = float(self.flight_price)
		except (ValueError,TypeError):
			flight_price = 0.0
		# try:
    	# 	flight_price = float(self.flight_price)
		# except (ValueError, TypeError):
    	# 	flight_price = 0.0

		self.total_price=total + flight_price
	
	def check_capacity(self):

		if self.flight:
			flight = frappe.get_doc("Airplane Flight", self.flight)
			airplane = frappe.get_doc("Airplane", flight.airplane)

			capacity = airplane.capacity
			ticket_count = frappe.db.count("Airplane Ticket", {"flight": self.flight})

			if ticket_count >= capacity:
				frappe.throw(f"Cannot book ticket. Flight is full ({capacity} seats already booked).")
