# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
#import NestedSet
from frappe.utils.nestedset import NestedSet

# make the class Test inherit from the NestedSet
class Test(NestedSet):
	nsm_parent_field = 'parent_tree'

# comment out the class that inherits from document
# class Test(Document):
# 	pass
