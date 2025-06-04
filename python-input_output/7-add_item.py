#!/usr/bin/python3
"""
This script adds command-line arguments to
a list and saves them to add_item.json.
"""
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# check the file has any items
if os.path.exists(filename):
    items = load_from_json_file(filename)  # convert to python object
else:
    items = []

# add command-line arguments to the list, exclude the script name
items.extend(sys.argv[1:])

# convert data back to json format
save_to_json_file(items, filename)
