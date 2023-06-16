# # Exercise 1
#
# user_list = [2, 3, 4, 4.6, 10]
#
#
# def product_integers_elements():
#     elements_product = 1
#     # for i in user_list:
#     #     if i % 2 == 0 or i % 3 == 0:
#     #         elements_product *= i
#     for i in user_list:
#         elements_product *= i
#     return elements_product
#
#
# print(product_integers_elements())
#
# =============================================================================
#
# # Exercise 2
#
# user_list = [2, 3, -4, -8]
#
#
# def min_from_list():
#     min(user_list)
#     # list_with_int_digits = []
#     # for i in user_list:
#     #     if type(i) == int:
#     #         list_with_int_digits.append(i)
#     return min(user_list)
#
#
# print(f'Min digit from list is ', min_from_list())
#
# =============================================================================
#
# # Exercise 3
#
# user_list = [2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 45, 55, 110, 125, 132, 220, 340, 1055, 1130, 123867432]
# # этот вариант криво работающий, на большее не хватило "фантазии" 8-)
#
# def prime_numbers_list():
#     count2 = user_list.count(2)
#     count_of_prime_digits = 0
#     for i in user_list:
#         if i / 1 == i and i / i == 1 and i % 2 != 0 and i % 5 != 0:
#             count_of_prime_digits += 1
#             if i % 5 == 0:
#                 count_of_prime_digits -= 1
#     return count_of_prime_digits + count2
#
#
# print(prime_numbers_list())
#
# ============================================================================
#
# # Exercise 4
#
# user_list = [1, 2, 3, 2, 3, 2, 3]
#
#
# def delete_given_number():
#     digits_entered_by_user = int(input('Enter the digits to remove: '))
#     count_of_removes = 0
#     for i in user_list:
#         if i == digits_entered_by_user:
#             user_list.remove(digits_entered_by_user)
#             count_of_removes += 1
#     return count_of_removes
#
#
# print(f'Count of deleted digits is', delete_given_number())
#
# =============================================================================
#
# # Exercise 5
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
#
# def concatenation_of_lists():
#     list1.extend(list2)
#     return list1
#
#
# print(concatenation_of_lists())
#
# =============================================================================
#
# Exercise 6
#
# user_list_enter = [1, 2, 3]
# user_choice_degree = 3
# new_list_degree = []
#
#
# def degree_of_elements():
#     for i in user_list_enter:
#         s = i ** user_choice_degree
#         new_list_degree.append(s)
#     return new_list_degree
#
#
# print(degree_of_elements())
