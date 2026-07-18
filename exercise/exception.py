# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("Don't division by zero")


# while True:
#     first_number=input('\nEnter first number:')
#     if first_number=='q':
#         break
#     second_number=input('Enter second number:')
#     if second_number=='q':
#         break
#     try:
#         int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('Division by zero')
#     else:
#         print(int(first_number) / int(second_number))

# from pathlib import Path
#
# def count_numbers_of_char(path):
#     """计算文件里有多少字符"""
#
#     try:
#         content = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print('File not found')
#     else:
#         word = content.split()
#         num_word = 0
#         for words in word:
#             print(words)
#             num_word += len(words)
#         print(num_word)
#
# path=Path('file_pi.txt')
# count_numbers_of_char(path)