// this is the js file that allows the doctype to be viewed as a tree

// ensure that the file is name as <name_of_doctype>_tree.js
// example this doctype is Test hence the name of this file is test_tree.js
// where test is the name of the doctpe in lower case

// add the code below to the tree

frappe.treeview_settings["Test"] = {
	ignore_fields:["parent_test"]
}