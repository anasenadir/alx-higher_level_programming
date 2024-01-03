#!/usr/bin/python3

def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): the string to be printed
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    flag_founded = False
    for w in text:
        if (w == ":" or w == "?" or w == "."):
            print("{}\n".format(w))
            flag_founded = 1
            continue
        
        if (flag_founded == 1 and w == " "):
            continue
        print(w, end='')
        flag_founded = 0
        
