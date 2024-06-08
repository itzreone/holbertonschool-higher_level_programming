#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of /
these characters: ., ? and :"""


def text_indentation(text):
    """
    Function printing text with two blank lines after each of ?, : and .
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")), end="")
