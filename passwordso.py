# IMPORTS #
import re


special_chars = ''

# A list of values for the min count of each type of char : starts off with required length of password

required_length = 10
required_lower_count = 1
required_upper_count = 1
required_digit_count = 1
required_special_count = 1


req_filename = "reqs.txt"


def load_requirements(req_file):
    with open(req_file, "r") as file:
        contents = file.readlines()
        for line in contents:
            components = line.split(' ')
            if component[0] == "password_length":
                required_length = int(component[2])
            elif component[0] == "digit_count":
                required_digit_count = int(component[2])
            elif component[0] == "lowercase_count":
                required_lower_count = int(component[2])
            elif component[0] == "uppercase_count":
                required_digit_count= int(component[2])
            elif component[0] == "special_count":
                required_special_count = int(component[2])


def init():
    print("Initialising")
    load_requirements(req_filename)
