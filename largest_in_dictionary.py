#! /usr/bin/python3
# Given a dictionary; How to get the key of the largest value
# Sample dictionary 
fruit_basket = {'apple': 4, 'orage': 2, 'banana': 8, 'mango': 5, 'peach': 7, 'avacado': 3}
max_fruit = max(fruit_basket, key=fruit_basket.get)
print("The fruit basket has {} {}".format(fruit_basket[max_fruit], max_fruit)) 
