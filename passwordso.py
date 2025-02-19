# IMPORTS #
import re


special_chars = ''

# A list of values for the min count of each type of char : starts off with required length of password
reqs = [] # length, lower, upper, digit, special

req_filename = "reqs.txt"


def load_requirements(req_file):
    with open(req_file, "r") as file:
        contents = file.readlines()
        for line in contents:
            reqs.append(int(line))

def init():
    print("Initialising")
    load_requirements(req_filename)
