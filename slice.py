player=['a','b','c','b','e','f']
# print(player[1:4])
# for p in player[:3]:
#     print(p.title())
player_1=player[:]
player.append('g')
player_1.append('h')
print(player)
print(player_1)