# Exercise 1

# n = [2, 4, -7]
# sum_neg_numb = 0
# sum_multiple_numb = 0
# sum_even_numb = 0
# sum_index_three = 1
# sum_poz_min_to_max = 0
#
# for i in n:
#     if i < 0:
#         sum_neg_numb += i
# print('Count of negative digits is', sum_neg_numb)
#
# for i in n:
#     if i % 2 == 0:
#         sum_multiple_numb += i
# print('Sum of multiple digits is ', sum_multiple_numb)
#
# for i in n:
#     if i % 2 != 0:
#         sum_even_numb += i
# print('Count of even numbers is', sum_even_numb)
#
# for i in n:
#     if i % 3 == 0:
#         sum_index_three *= i
# print('Product of multiples of three', sum_index_three)
#
# print('Product of elements between minimum and maximum element', min(n) * max(n))
#
# for i in n:
#     if i >= 0:
#         sum_poz_min_to_max += i
# print('The sum of the elements between the first and last positive elements', sum_poz_min_to_max)

# ==================================================================================

# Exercise 2

even_numbs = []
odd_numbs = []
neg_numbs = []
pos_numbs = []

n = [2, 3, 7, 8, -3, -12]

for i in n:
    if i % 2 == 0:
        even_numbs.append(i)
print('Even numbers is', even_numbs)

for i in n:
    if i % 3 != 0:
        odd_numbs.append(i)
print('Odd numbers is', odd_numbs)

for i in n:
    if i <= 0:
        neg_numbs.append(i)
print('Negative numbers is', neg_numbs)

for i in n:
    if i >= 0:
        pos_numbs.append(i)
print('Positive numbers is', pos_numbs)
