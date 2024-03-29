#!/usr/bin/python3
""" function that creates an Object from a “JSON file”.
"""
from sys import argv
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_name = "add_item.json"
json_list = []


if (path.exists(file_name)):
    json_list = load_from_json_file(file_name)

json_list.extend(argv[1:])
save_to_json_file(json_list, file_name)
