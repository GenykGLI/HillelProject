# Exercise 1
#
# user_list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
# # sort_list = []
# # for i in user_list:
# #     if i not in sort_list:
# #         sort_list.append(i)
# # print('Removed duplicates from the list', sort_list)
#
# sort_list_v2 = list(set(user_list))
# print('Removed duplicates from the list', sort_list_v2)
# =========================================================

# Exercise 2

# user_list1 = input('Enter the list of digits 1: ')  # 1232423524
# user_list2 = input('Enter the list of digits 2: ') # 2342342353
#
# countlist1 = list(user_list1)
# countlist2 = list(user_list2)
# # user_list = [1, 2, 3]
# # user_list2 = [1, 2, 3]
# # print('In the 1-st list is', len(user_list), ', in the 2-nd is', len(user_list2))
#
# print('In the 1-st list is', len(countlist1), ', in the 2-nd is', len(countlist2))

# Exercise 3
#
# a = ''' 4
# Был жаркий летний день. Солнце светило ярко. Небо было голубое.
# Три девочки Катя, Марина и Юля собирали в поле цветы.
# Они набрали по букету разных цветов ромашки, васильки, одуванчики.
# А потом сплели из полевых цветов красивые венки на голову.'''
#
# wordcount = 0
# a = a.split()
# # print(len(a))
#
# for i in range(len(a)):
#     if i != ', ' and i != '. ' and i != ' ':
#         wordcount += 1
# print(wordcount)
