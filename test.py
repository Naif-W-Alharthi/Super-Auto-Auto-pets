


dice_art = ["""
 -------
| Damage   hp   |
|   UN   |
|       |
 ------- ""","""
 -------
|       |
|   1   |
|       |
 ------- """]

base_upper=" ---------"
base_upo_middle = " |   P   |"
base_middle = " |   N   |"
base_low_middle = " |  d  h  |"
base_lower=" ---------"

#use this code just format it better
player = [0, 1]
lines = [dice_art[i].splitlines() for i in player]
for l in zip(*lines):
    print(*l, sep='')

