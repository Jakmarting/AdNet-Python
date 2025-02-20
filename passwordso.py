# IMPORTS #
import re
import random
import string

special_chars = '@_!#$%^&*()<>?/\|}{~:'

# A list of values for the min count of each type of char : starts off with required length of password

required_length = 10
required_lower_count = 1
lower_re = re.compile(r'[a-z]')
required_upper_count = 1
upper_re = re.compile(r'[A-Z]')
required_digit_count = 1
digit_re = re.compile(r'[0-9]')
required_special_count = 1
special_re = re.compile(f"{special_chars}")


req_filename = "reqs.txt"
poor_passwords_filename = "poor.txt"
poor_passwords = []

def load_requirements(req_file):
    try:
        with open(req_file, "r") as file:
            contents = file.readlines()
            for line in contents:
                components = line.split(' ')
                if components[0] == "password_length":
                    required_length = int(components[2])
                elif components[0] == "digit_count":
                    required_digit_count = int(components[2])
                elif components[0] == "lowercase_count":
                    required_lower_count = int(components[2])
                elif components[0] == "uppercase_count":
                    required_digit_count= int(components[2])
                elif components[0] == "special_count":
                    required_special_count = int(components[2])
    except FileNotFoundError:
        pass

    
    try:
        with open(poor_passwords_filename, "r"):
            poor_passwords = file.readlines()
    except FileNotFoundError:
        pass


def check_password_against_requirements(chk_password):

    strength = 0
    requirement_msgs = []
    
    if len(chk_password) >= required_length:
        strength += 1
    else:
        strength -= 1
        requirement_msgs.append(f'Your password does not meet the required length of: {required_length}')


    if len(lower_re.findall(chk_password)) >= required_lower_count:
        strength += 1
    else:
        requirement_msgs.append(f'Your password does not meet the required count of lower case chars: {required_lower_count}')


    if len(upper_re.findall(chk_password)) >= required_upper_count:
        strength += 1
    else:
        requirement_msgs.append(f'Your password does not meet the required count of upper case chars: {required_upper_count}')


    if len(digit_re.findall(chk_password)) >= required_digit_count:
        strength += 1
    else:
        requirement_msgs.append(f'Your password does not meet the required count of digits: {required_digit_count}')

        
    if len(special_re.findall(chk_password)) >= required_special_count:
        strength += 1
    else:
        requirement_msgs.append(f'Your password does not meet the required count of special chars: {required_special_count} special chars are: {special_chars}')

    if chk_password in poor_passwords:
        strength = 0
        requirement_msgs.append(f'Your password has been previously flagged as unsafe: this is likely a commonly used password or has been included in a data breach')

    return strength, requirement_msgs
    

def generate_password():

    generate_password = []

    for i in range(required_lower_count):
        generate_password.append(random.choice(list(string.ascii_lowercase)))
        
    for i in range(required_upper_count):
        generate_password.append(random.choice(list(string.ascii_uppercase)))

    for i in range(required_digit_count):
        generate_password.append(random.choice(list(string.digits)))
        
    for i in range(required_special_count):
        generate_password.append(random.choice(list(special_chars)))
        
    allowed_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(special_chars)
    
    while len(generate_password) < required_length:
        generate_password.append(random.choice(allowed_chars))

    random.shuffle(generate_password)
    
    return ''.join(generate_password)

def init():
    print("Initialising...")
    load_requirements(req_filename)
