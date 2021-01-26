#! /usr/bin/python3
# Example on getting input during script execution using argparse
# Sample: argparse_example.py --name Tony --age 45 --height 170 --weight 165

import argparse

parser = argparse.ArgumentParser(description="Obtain person's data")

help_name = "person's name "
format_name = "Sample: --name Steve"

help_age = "person's age "
format_age = "Sample: --age 34"

help_height = "person's height "
format_height = "Sample: --height 178"

help_weight = "person's weight "
format_weight = "Sample: --weight 185"

mandatory = parser.add_argument_group(title="MANDATORY ARGUMENTS")
mandatory.add_argument("--name",dest='name',required=True,help=help_name+format_name)
mandatory.add_argument("--age",dest='age',required=True,help=help_age+format_age)
mandatory.add_argument("--height",dest='height',required=True,help=help_height+format_height)
mandatory.add_argument("--weight",dest='weight',required=True,help=help_weight+format_weight)

args = parser.parse_args()

print("Person named {} is {} years old.\nHe/She is {}cm tall and weighs {}lbs.".format(args.name, args.age, args.height, args.weight))