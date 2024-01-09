#!/usr/bin/python3
""" function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”.

    Args:
        filename (str): _description_
    """
    with open(filename, mode="r", encoding="utf-8") as fd:
        return json.load(fd)
