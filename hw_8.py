# Exercise 1

def degree_of_number(number):
    if number <= 1:
        return 1
    return number * number + degree_of_number(number - 1)


print(f'The sum of number degree in recursion is', degree_of_number(6))


################################################################

# Exercise 2

# def sum_stars(x):
#     if x <= 1:
#         return 1
#     return x + sum_stars(x - 1)
#
#
# def print_stars():
#     count_stars = int(input('Enter the sum of stars: '))
#     print(sum_stars(count_stars) * '*', end=' ')
#
#
# print_stars()


################################################################


# Exercise 3


# def sum_of_digits(range_a, range_b, count=0):
#     if range_a > range_b:
#         return count
#     count += range_a
#     return sum_of_digits(range_a + 1, range_b, count)
#
#
# def range_numbers():
#     range_a = int(input('Enter initial number: '))
#     range_b = int(input('Enter end number: '))
#     print(sum_of_digits(range_a, range_b))
#
#
# range_numbers()

################################################################

