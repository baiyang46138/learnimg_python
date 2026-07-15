# name ="Ada lovelace"
# print(name.title())首字母大写
# print(name.upper())
# print(name.lower())
# first_name="ada"
# last_name="lovelace"
# full_name=f"{first_name} {last_name}"
# print(full_name)
# print(f"hello,{full_name.title()}!")
# message=f"hello,{full_name.title()}!"
# print(message)
# print("python")
# print("\tpython")
# print("Languages:\npython\nc\njavascript")
# print("Languages:\n\tpython\n\tc\n\tjavascript")
# f_l=' ptython '
# print(f_l)
# print(f_l.rstrip())
# print(f_l.lstrip())
# print(f_l.strip())删除空格
# url='https://nostarch.com'
# print(url.removeprefix('https://'))
# import this
from name_test import get_formatted_name

while True:
    first_name=input("Enter your first name: ")
    if first_name.lower()=="q":
        break
    last_name=input("Enter your last name: ")
    if last_name.lower()=="q":
        break

    format_name=get_formatted_name(first_name,last_name)
    print(format_name)

