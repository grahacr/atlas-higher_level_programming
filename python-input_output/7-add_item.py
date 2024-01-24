#!/usr/bin/python3
""" module contains script for creating json file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    new_file = load_from_json_file('add_item.json')
except FileNotFoundError:
    new_file = []
for arg in sys.argv[1:]:
    new_file.append(arg)
save_to_json_file(new_file, 'add_item.json')