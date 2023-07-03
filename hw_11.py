# Exercise 1

# input_file = 'input.txt'
# output_file = 'output.txt'
#
# with open(input_file, 'r') as file:
#     text = file.read()
#     words = text.split()
#
#     filtered_words = [word for word in words if len(word) >= 7]
#
#     with open(output_file, 'w') as output:
#         output.write('\n'.join(filtered_words))
#
# print('Words in which 7 or more letters are written to the file','"', output_file, '"')

###############################################################################################

# Exercise 2

user_file = 'user_text.txt'

with open(user_file, 'r') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)

print('count of words in text is', word_count)
