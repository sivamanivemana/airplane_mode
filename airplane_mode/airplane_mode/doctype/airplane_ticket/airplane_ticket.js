// Copyright (c) 2023, Rohit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	// refresh: function(frm) {

	// }
});

// frappe.listview_settings['Sales Order'] = {
// 	add_fields: [
// 		"naming_series",
// 		"passenger",
// 		"flight",
// 		"source_airport",
// 		"destination_airport",
// 		"source_airport_code",
// 		"destination_airport_code",
// 		"depart_date",
// 		"depart_time",
// 		"duration",
// 		"status"
// 	   ],
// 	get_indicator: function (doc) {

// 		if (doc.status === "Booked") {
// 			// Closed
// 			return [__("Closed"), "gray", "status,=,Booked"];
// 		} else if (doc.status === "Checked-In") {
// 			// on hold
// 			return [__("Checked-In"), "purple", "status,=,Checked-In"];
// 		} else {
// 			// not billed
// 			return [__("Boarded"), "green", "status,=,Booked"];
// 		}
// 	}
// }