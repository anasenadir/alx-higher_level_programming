#!/usr/bin/python3

def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): the string to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])
        
