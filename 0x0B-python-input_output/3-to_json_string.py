#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """_summary_

    Args:
        my_obj (_type_): _description_
    """
    return json.dumps(my_obj)
