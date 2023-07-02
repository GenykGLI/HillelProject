# Exercise 4

import re


def validate_password(psd):
    result = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*+]).{8,16}$'
    return re.search(result, psd)


password = 'Qwerty1234@'
if validate_password(password):
    print('Confirm syntax password')
else:
    print('Incorrect syntax password')

# def validate_password(pwd):
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])' \
#               r'(?=.*[a-zA-Z\d@#$%^&+=!]).{8,16}$'
#     return re.match(pattern, pwd) is not None
#
#
# password = "Abcd1234@"
# if validate_password(password):
#     print("Пароль валиден")
# else:
#     print("Пароль невалиден")
