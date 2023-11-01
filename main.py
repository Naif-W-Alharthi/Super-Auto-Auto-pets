import tensorflow as tf

class match_env:
    def __init__(self):
        pass
    #turn is something adding up as a count 
        
class Unit:
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.Hp = Hp
        self.Damage = Damage
        self.Cost =3 
        self.level=1
        self.Sell_price=1*self.level
        self.perk = None
        self.state="Alive"

    def damage_unit(self,damage):
        self.Hp = self.Hp - damage
        if self.Hp <= 0:
            self.state="Faint"

    def alive_check(self):
        return self.state =="Alive"
class Board:
    def __init__(self,units):
        self.order = []
        for unit in units:
            self.order.append(unit)
    def show_order(self):
        for position,units in enumerate(self.order[::-1]):
            self.order.append(units)
            print(position,units.Name, units.Hp, units.Damage)
    def amount_units(self):
        return len(self.order)
    def remove_fainted_list(self):
        
        self.order = [x for x in self.order if not x.alive_check()]
        
    # def moveup(self):
        # for unit in self.order:
        #     unit
        
def battle_phase(board1,board2):
    # print(board1.show_order(),board2.show_order())
    ##pre battle stuff WIP
    ###

    #mid attacl
    board1.order[0].damage_unit(board2.order[0].Damage)
    board2.order[0].damage_unit(board1.order[0].Damage)

    #post attack
    board1.remove_fainted_list()
    board2.remove_fainted_list()

    #results
    print
    if board1.amount_units() == 0 and  board2.amount_units()!=0:
        print("board 1 wins")
    elif board1.amount_units() != 0 and board2.amount_units()==0:
        print("board 2 wins")
    else:
        print("draw")
    ##

    

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
    print("======================")
    print("======================")
    board1.show_order()
    print("======================")
    board2.show_order()
otter= Unit("otter",1,3)

rat= Unit("rat",1,3)
first_board = Board([otter])
otter_buffed= Unit("otter",2,3)
second_board = Board([otter_buffed,rat])
display_board(first_board,second_board)