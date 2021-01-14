#! /usr/bin/python3
import re
# Compile a pattern that matches every character that is not an alphabet (i.e a-z A-Z)
pattern = re.compile('[^a-zA-Z]')
# Example string
sentence = "Punctuation matters: Eat your dinner! vs Eat. You're dinner!"
print("Sentence before removing non alphabets: {}".format(sentence))
# Substituting every non alphabet with ''
result = pattern.sub('', sentence)
print("Sentence with only alphabets: {}".format(result))
