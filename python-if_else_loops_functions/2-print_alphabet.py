#!/usr/bin/python3
letter = "a"
output = ""
while letter < "z":
    output += letter
    letter = chr(ord(letter) + 1)
print(output)
