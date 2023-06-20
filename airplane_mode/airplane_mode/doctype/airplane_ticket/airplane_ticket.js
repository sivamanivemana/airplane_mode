// Copyright (c) 2023, Rohit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket Add-on Item', {
	item: function(frm) {

		var tbl = frm.doc.add_ons || [];
		var i = tbl.length - 1;
		const last_element = tbl[i].item
		console.log(last_element)
		while (i--)
		{
	
			if(tbl[i].item == last_element)
				{
					cur_frm.get_field("add_ons").grid.grid_rows[i].remove();
					frappe.throw("Please add unique items only in add-ons")
				}
			
			cur_frm.refresh();
	
			}
		   }
		});






















//     validate: function(frm) {
//         var items = frm.doc.add_ons;
// 		console.log(items)
//         var uniqueItems = [];
//         var itemNames = [];

//         // Loop through each item in the child table
//         for (var i = 0; i < items.length; i++) {
//             var item = items.item[i];
// 			console.log(item);

//             // Check if the item name has already been added to the uniqueItems array
//             if (itemNames.indexOf(item.item_name) === -1) {
//                 uniqueItems.push(item);
//                 itemNames.push(item.item_name);
//             }
//         }

//         // Replace the items array with the uniqueItems array
//         frm.doc.items = uniqueItems;
//     }
// });










// frappe.ui.form.on('Airplane Ticket', {
// 	validate: function(frm) {
// 	  // get the child table
// 	  var child_table = frm.fields_dict['add_ons'].grid;
// 	  console.log(child_table)
  
// 	  // use distinct to remove duplicates
// 	  var distinct_rows = child_table.get_data().distinct(function(row) {
// 		return row.item;
// 	  });
  
// 	  // set the child table data to the distinct rows
// 	  child_table.grid_rows = [];
// 	  child_table.make_new_row();
// 	  child_table.df.data = distinct_rows;
// 	  child_table.refresh();
// 	}
//   });
  






// frappe.ui.form.on('Airplane Ticket', {
// 	validate: function(frm, cdt, cdn) {
// 	  var child_table = frm.doc.add_ons || [];
// 	  console.log(child_table)
// 	  var unique_values = {};
// 	  var to_remove = [];
  
// 	  for (var i = 0; i < child_table.length; i++) {
// 		var row = child_table[i];
// 		if (unique_values[row.field_to_check]) {
// 		  to_remove.push(row.name);
// 		} else {
// 		  unique_values[row.field_to_check] = true;
// 		}
// 	  }
  
// 	  for (var i = 0; i < to_remove.length; i++) {
// 		frappe.model.clear_doc("Airplane Ticket Add-on Item", to_remove[i], true);
// 	  }
// 	}
//   });








// frappe.ui.form.on('Airplane Ticket', {
	// 	refresh(frm) {
		// 	  var child_table = frm.fields_dict['add_ons'].grid;
		
		// 	  var unique_values = new Set();
  
// 	  child_table.grid_rows.forEach(function (row) {
// 		var field_value = row.get_field('item').value;
// 		if (unique_values.has(field_value)) {
// 		  row.remove();
// 		} else {
// 		  unique_values.add(field_value);
// 		}
// 	  });
// 	}
//   });



































// 	validate: function(frm, cdt, cdn) {
// 		var d = local[cdt][cdn];
// 		if d.

	// 	var tbl = frm.doc.add_ons || [];
	// 	var i = tbl.length;

	// 	while (i--)
	// 	{
	// 	    	if(tbl[i].item == 'Double Seat')
	// 	    	{
	// 	    	    cur_frm.get_field("add_ons").grid.grid_rows[i].remove();
	// 	    	}
	// 	}
	// 	cur_frm.refresh();

	// }
// });

// frappe.ui.form.on("Airplane Ticket", {
// 	validate: function(frm, cdt, cdn) {
// 		$.each(locals[cdt][cdn].add_ons, function(row) {
// 			console.log(row.item, cdt.item)
// 			if (row.item === cdt.item) {
// 				frappe.msgprint({
// 					title: (__('Duplicated Item')),
// 					indicator: 'red',
// 					message: (__('The item you added already exist in the table.'))
// 				});
// 				frappe.model.delete_doc(cdt, cdn);
// 				frm.refresh_field('add_ons');
// 				return false;
// 			}
// 		});
// 	}
// });











// frappe.ui.form.on("Add Ons", {
// 	item: function(frm,cdt,cdn) {
// 		var row = locals[cdt][cdn];
// 		if (row.item ){

// 		}

// 		}
// });


















// return arr.filter((item,
// 	index) => arr.indexOf(item) === index);



