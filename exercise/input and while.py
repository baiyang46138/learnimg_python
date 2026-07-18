# message=input("enter your message")
# print(message)
# name=input("Enter your name:")
# print(f"\nhello {name}")
# age=input("enter your age")
# age=int(age)
# if age>18:
#     print("you are old enough to deal with it")
# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1
# print(current_number)
# message=""
# while message!="quit":
#     message=input("prompt:")
#     if message!="quit":
#         print(message)
# active=True
# while active:
#     message=input("Enter a message:")
#     if message=="quit":
#         break
# #active=False
#     else:
#         print(message)
# curr_num=0
# while curr_num<10:
#     curr_num+=1
#     if curr_num%2==0:
#         continue
#     print(curr_num)
# unconfirmed_user=['a','b','c']
# confirmed_user=[]

# while unconfirmed_user:
#     curr_user=unconfirmed_user.pop()
#
#     print(f"verifying user:{curr_user.title()}")
#     confirmed_user.append(curr_user)
#
# for user in confirmed_user:
#     print(user)

# responses={}
# active=True
#
# while active:
#     name=input("\nwhat is your name? ")
#     response=input("what is your responses? ")
#
#     responses[name]=response
#
#     repeat=input("Would you like to let another person do this? (y/n) ")
#     if repeat=="n":
#         active=False
#
# for name,responses in responses.items():
#     print(f"{name} says {responses}")