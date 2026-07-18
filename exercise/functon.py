# def greet_user():
#     print("Hello user")
# greet_user()
# def describe_pet(pet_name,animal_type,pet_age=''):
#     print(animal_type)
#     print(pet_name)
#     print(pet_age)
# describe_pet('dog','bbs')
# describe_pet(pet_name='www',animal_type='dog')
# describe_pet(animal_type='cat',pet_name='by')
# describe_pet('cat','by','6')
# def build_person(first_name, last_name,age=None):
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('John', 'Doe',27)
# print(musician)
# def greet_user(names):
#     for name in names:
#         print(f"Hello, {name}!")
# usernames = ["a", 'b', "c", "d"]
# greet_user(usernames)
# def make_pizza(size,*toppings):
#     print(size)
#     for topping in toppings:
#         print(f"-{topping}")
# # print(toppings)
# make_pizza(12,'mushrooms','green peppers')
# import  pizza
# from  pizza import make_pizza as mp
# mp(16,'peppers')