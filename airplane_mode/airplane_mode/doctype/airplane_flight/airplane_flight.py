# Copyright (c) 2025, YASH GAUTAM and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	

	def  on_submit(self):

		self.db_set("status","Completed")

		
