import frappe
from airplane_mode.airplane_mode.utils import create_random

def execute():
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"seat": None},
        fields=["name"]
    )

    for ticket in tickets:
        seat = create_random()
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)
