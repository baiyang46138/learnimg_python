char_1=['a','b','c','d']
char_2=['a','b','c','d','e']
# for c in char_1:
#     if c=='b':
#         print(c)
#     else:
#         print(c.title())
# if 'b' in char_1:
#     print('yes')
# age=18
# if age>=18:
#     print("Yes")
# elif age>=12:
#     print("No")
# else:
#     print("Yes")
# if char_1:
#     for c in char_1:
#         print(c)
# else:
#     print('no value')
for c in char_2:
    if c in char_1:
        print(c)
    else:
        print(f"not a {c.title()}")