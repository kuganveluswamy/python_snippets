#! /usr/bin/python3
import re

# Example sentence
sentence = "Punctuation matters: Eat your dinner! vs Eat. You're dinner!"

# Method 1 using regex match
# Compile a pattern that matches every character that is not an alphabet (i.e a-z A-Z)
pattern = re.compile('[^a-zA-Z]')
print("Sentence before removing non alphabets: {}\n".format(sentence))
# Remove every non alphabet with substitution
result = pattern.sub(' ', sentence)
print("Regex Method >\n Sentence with only alphabets: {}".format(result))

# Method 2 using isaplha()
result = ''.join([letter if letter.isalpha() else ' ' for letter in sentence])
print("isaplha() Method >\n Sentence with only alphabets: {}".format(result))
