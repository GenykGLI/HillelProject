import re


# Exercise 1

# def validate_mobile_number(number):
#     result = re.search(r'^\+?\d{10,13}$', number)
#     print(result)
#
#
# def user_validate_mobile_number():
#     user_input = input('Enter phone number: ')
#     validate_mobile_number(user_input)   # For example:  +380631234567
#
#
# user_validate_mobile_number()

##################################################################################################

# Exercise 2


# def validate_home_number(number):
#     result = re.search(r'^\d{4,8}$', number)
#     print(result)
#
#
# def user_validate_home_number():
#     user_input = input('Enter phone number: ')      # For example  7445656
#     validate_home_number(user_input)
#
#
# user_validate_home_number()

##################################################################################################

# Exercise 3


def validate_email(email):
    result = re.search(r'^\w+@\w+\.\w{2,4}$', email)
    print(result)


def user_validate_email():
    user_input = input('Enter your email: ')  # For example   example@gmail.com
    validate_email(user_input)


user_validate_email()
