


# dice_art = ["""
#  -------
# | Damage   hp   |
# |   UN   |
# |       |
#  ------- ""","""
#  -------
# |       |
# |   1   |
# |       |
#  ------- """]

# base_upper=" ---------"
# base_upo_middle = " |   P   |"
# base_middle = " |   N   |"
# base_low_middle = " |  d  h  |"
# base_lower=" ---------"

# #use this code just format it better
# player = [0, 1]
# lines = [dice_art[i].splitlines() for i in player]
# for l in zip(*lines):
#     print(*l, sep='')
# import numpy as np 
# cjhec = ["a","b","c"]
# list_ally_index = np.random.choice(cjhec, size=2, replace=False)

# print(list_ally_index)

x = [2]  # Using a list to hold the integer value

def add_2(r):
    r[0] += 59  # Modifying the value inside the list

add_2(x)
print(x[0])  #