#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj (obj): the object to be serialized
        filename (str): the file to wirte the serialized object in
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
