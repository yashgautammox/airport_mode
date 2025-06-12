# Copyright (c) 2025, YASH GAUTAM and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	chart = get_chart_data(data)

	print("This is data ",data)

	print("This Is columns ",columns)
	return columns, data ,None , chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150
        }
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""

	row = frappe.db.sql("""
		SELECT
        airline.name AS airline,
        IFNULL(SUM(total_price), 0) AS revenue
        FROM `tabAirline` airline
        LEFT JOIN `tabAirplane` airplane ON airplane.airline = airline.name
        LEFT JOIN `tabAirplane Flight` flight ON flight.airplane = airplane.name
        LEFT JOIN `tabAirplane Ticket` ticket ON ticket.flight = flight.name AND ticket.docstatus = 0
        GROUP BY airline.name
        ORDER BY revenue DESC
					  """,as_list = True)


	return row	

def get_chart_data(data):
    labels = [row[0][:10] + '…' if len(row[0]) > 10 else row[0] for row in data]
    values = [row[1] for row in data]
    return {
        "data": {
            "labels": labels,
            "datasets": [{"values": values}]
        },
        "type": "donut",
        "height": 300
    }
