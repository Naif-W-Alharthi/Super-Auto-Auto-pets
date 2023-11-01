import tensorflow as tf
# import random
from numpy.random import seed
from numpy.random import randint
import numpy as np
class match_env:
    def __init__(self):
        pass
    #turn is something adding up as a count 


def otter_ability(otter):
    ##when bought give random ally +1*lvl hp 
    pass
def mosquito_ability(mosquito):
    action_phase = "pre_combat"


def ant_ability(ant,owner_board):
    if ant.ability_flag == True:
        buff_amount = ant.level
        owner_board.random_ally_single().buff(buff_amount,buff_amount)


def duck_ability(duck,shop_board):
    pass
    

##stack order
#1)hurt (alive units get pirio)
#2)faint (by which one dies first) (tie is broken by left to right on player side?)
#

ability_dict ={"ant":[ant_ability,"faint"],"otter":[otter_ability,"buy"],"mosquito":[mosquito_ability,"start_of_round"],"duck":[otter_ability,"buy"]} 

class Unit:
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.Hp = Hp
        self.Damage = Damage
        self.Cost =3 
        self.level=1
        self.Tier=1
        self.Sell_price=1*self.level
        self.perk = None
        self.state="Alive"
        self.ability=ability_dict[Name][0]

        self.activation_condition(ability_dict[Name][1])
        self.ability_limit=0
        # self.ability_flag

    def update(self):
        self.activation_condition([0])
    def attack(self,enemy):
        enemy.Hp = enemy.Hp - self.Damage
        self.Hp = self.Hp - enemy.Damage
        print(self.Name, " attacked ",enemy.Name )
        print(enemy.Name, " attacked ",self.Name )
        if enemy.Hp <= 0:
            enemy.state="Faint"
        if self.Hp <= 0:
            self.state="Faint"
            # if type=="faint":
            #     if self.alive_check == False:
            #         self.ability_flag= True
            #         print("This activates passively")

    def alive_check(self):
        return self.state =="Alive"
    def buff(self,Damage,Hp):
        self.Hp = self.Hp+Hp
        self.Damage=self.Damage + Damage

    def activation_condition(self,type):
        if type=="faint":
            if self.alive_check == False:
                self.ability_flag= True
                print("This activates passively")

    
class Board:
    def __init__(self,units):
        self.order = []
        self.attack_que =[]
        for unit in units:
            self.order.append(unit)
    def show_order(self):
        for position,units in enumerate(self.order[::-1]):
            self.order.append(units)
            # print(position,units.Name, units.Hp, units.Damage)
    
    def amount_units(self):
        return len(self.order)
    def remove_fainted_list(self):
       
        
        self.order = [x for x in self.order if  x.alive_check()]
        # print(self.order[0].alive_check())
    def show_order_display(self):
        for position,units in enumerate(self.order[::-1]):
            # self.order.append(units)
            print(f""" -----{position}---\n|    {units.Name}    |\n|damage:{units.Damage}||hp:{units.Hp}|""")
            
    def random_ally(self,num_ally):

        list_ally_index = np.randint(0,self.amount_units(),num_ally)
            
        return list_ally_index
        
    def random_ally_single(self):

        list_ally_index = np.randint(0,self.amount_units(),1)
            
        return self.order[list_ally_index[0]]
    def update_board(self):
        ###careful of order
        for unit in self.order:
            unit.update()
    def add_unit_attack_q(self,unit):
        pass
    # def moveup(self):
        # for unit in self.order:
        #     unit

def battle_phase(board1,board2):
    # print(board1.show_order(),board2.show_order())
    battle_finished = False
    round_count= 0
    while not battle_finished:
        ##pre battle stuff WIP
        ###
        round_count= 1+round_count
        #mid attacl
        
        print("======================")
        print("┃                    ┃")
        print("┃      round  ",round_count,"    ┃")
        print("┃                    ┃")
        print("======================")
        board2.order[0].attack(board1.order[0])
        # board1.update()
        # board1.update()
        
        #post attack
        board1.remove_fainted_list()
        board2.remove_fainted_list()
        board1.update_board()
        board2.update_board()
        # results
        # print(board1.amount_units())
        # print(board2.amount_units())

        if board1.amount_units() == 0 and  board2.amount_units()!=0:
            print("board 2 wins")
            battle_finished = True
            # return ("Lost")
        elif board1.amount_units() != 0 and board2.amount_units()==0:
            print("board 1 wins")
            battle_finished = True
            # return ("Win")
        
        elif board1.amount_units() == 0 and board2.amount_units()==0:
            print("draw")
            battle_finished = True
            # return "draw"
        else:
            continue
        
    ##

    

class Unit_store:
    def __init__(self,turn,units):
        self.units= units
        
def display_board(board1,board2):
    # while add loops here for gods sake 

    turns = 0

    print("======================")
    print("┃                    ┃")
    print("┃        V   S       ┃")
    print("┃                    ┃")
    print("======================")
    print("board 1")
    board1.show_order_display()
    print("""===========  \n_ _ ___ \n| | |_ -|\n\_/|___|\n===========""")
    print("board 2")
    board2.show_order_display()
    battle_phase(board1,board2)
    # print("======================")
    # print("┃                    ┃")
    # print("┃       Round 2      ┃")
    # print("┃                    ┃")
    # print("======================")
    # print("board 1")
    # board1.show_order_display()
    # print("======================")
    # print("board 2")
    # board2.show_order_display()
    

otter= Unit("otter",4,3)

ant= Unit("otter",1,3)
ant1= Unit("otter",1,3)
first_board = Board([otter,ant,ant1])
otter_buffed= Unit("duck",4,3)
otter_buffed1= Unit("duck",3,1)
otter_buffed2= Unit("duck",2,1)
second_board = Board([otter_buffed,otter_buffed1,otter_buffed2])
display_board(first_board,second_board)