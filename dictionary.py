# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# alien_0['x_position']=0
# alien_0['y_position']=25
# print(alien_0)
# alien_0["color"]='blue'
# print(alien_0)
# del alien_0['points']
# print(alien_0)
# p=alien_0.get('points')
# print(p)
# user_0={
#     'name':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }
# for key,value in user_0.items():
#     print(f"\nkey:{key}")
#     print(f"value:{value}")
# for k in user_0.keys():
#     print(k)
#
# for k in sorted(user_0.keys()):
#     print(k)
# for v in set(user_0.values()):
#     print(v)
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 5}
# alien_2 = {'color': 'red', 'points': 5}
#
# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)
aliens=[]

# for alien_number in range(30):
#     new_alien={'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)

# for i in aliens[:5]:
#     print(i)
# print(f"number:{len(aliens)}")
# for alien in aliens[:3]:
#     if alien['color']=='green':
#         alien['color']='yellow'
#         alien['points']=10
#         alien['speed']='fast'
# for i in aliens[:5]:
#     print(i)
# print(f"number:{len(aliens)}")
# pizza={
#     'crust':'thick',
#     'toppings':['mushroom','cheese']
# }
# for k,v in pizza.items():
#     if len(v) != 1:
#         for l in v:
#             print(l)
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print(f"username:{username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")