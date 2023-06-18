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
s = [2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 45, 55, 59]
lst = []


def find(a):
    poz = 0
    for i in range(1, a + 1):
        if a % i == 0:
            poz += 1
    if poz == 2:
        lst.append(a)


def check():
    for i in s:
        find(i)
    print(f'Count of prime numbers is ', len(lst))


check()

#
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
