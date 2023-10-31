import tensorflow as tf


class Unit:
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.Hp = Hp
        self.Damage = Damage
        self.Cost =3 
        self.level=1
        self.Sell_price=1*self.level
        self.perk = None

class Board:
    def __init__(self,units):
        self.order = []
        for unit in units:
            self.order.append(unit)
    def show_order(self):
        for position,units in enumerate(self.order[::-1]):
            print(position,units.Name, units.Hp, units.Damage)

def battle_phase(board1,board2):
    print(board1.order,board2.order)

class Unit_store:
    def __init__(self,turn,units):
        self.units= units
        
def display_board(board1,board2):
    print("======================")
    print("┃                    ┃")
    print("┃        V   S       ┃")
    print("┃                    ┃")
    print("======================")
    board1.show_order()
    print("======================")
    board2.show_order()
    print("======================")
    print("┃                    ┃")
    print("┃       Round 1      ┃")
    print("┃                    ┃")
    print("======================")
    battle_phase(board1,board2)

otter= Unit("otter",1,3)

rat= Unit("rat",1,3)
first_board = Board([otter])
otter_buffed= Unit("otter",2,3)
second_board = Board([otter_buffed,rat])
display_board(first_board,second_board)