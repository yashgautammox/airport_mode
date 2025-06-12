// Copyright (c) 2025, YASH GAUTAM and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
		frm.add_custom_button("Assign Seat", () => {
			let d = new frappe.ui.Dialog({
				title: 'Enter Seat Number',
				fields: [
					{
						label: 'Seat Number',
						fieldname: 'seat_number',  // ✅ lowercase 'n' in 'fieldname'
						fieldtype: 'Data',
						reqd: 1
					}
				],
				primary_action_label: 'Assign',
				primary_action(values) {
					frm.set_value('seat', values.seat_number);
					d.hide();
				}
			});
			d.show();
		}, "Actions");
	}
});
