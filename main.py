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
        owner_board.random_ally_single().temp_buff(buff_amount,buff_amount)
        


def duck_ability(duck,shop_board):
    pass
    
# def board_cleanup(board1,board2):
#     board1
##stack order
#1)hurt (alive units get pirio)
#2)faint (by which one dies first) (tie is broken by left to right on player side?)
#

ability_dict ={"ant":[ant_ability,"faint"],"otter":[otter_ability,"buy"],"mosquito":[mosquito_ability,"start_of_round"],"duck":[otter_ability,"buy"]} 

class Unit:
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.round_hp = Hp
        self.base_Hp = Hp
        self.Damage = Damage
        
        self.Cost =3 
        self.level=1
        self.Tier=1
        self.Sell_price=1*self.level
        self.perk = None
        self.state="Alive"
        self.ability=ability_dict[Name][0]
        self.temp_buff_hp = 0
        self.temp_buff_damage= 0
        self.activated_flag = False
        self.activation_condition_var = ability_dict[Name][1]
        
        self.ability_limit=0
        self.ability_flag=False

    def update(self):
        # print(self.activation_condition_var)
        self.activation_condition(self.activation_condition_var)
    def attack(self,enemy):
        enemy.round_hp = enemy.round_hp - self.Damage
        self.round_hp = self.round_hp - enemy.Damage
        print(self.Name, " attacked ",enemy.Name )
        print(enemy.Name, " attacked ",self.Name )
        if enemy.round_hp <= 0:
            enemy.state="Faint"
        if self.round_hp <= 0:
            self.state="Faint"
            # if type=="faint":
            #     if self.alive_check == False:
            #         self.ability_flag= True
            #         print("This activates passively")

    def alive_check(self):
        return self.state =="Alive"
    def perma_buff(self,Damage,Hp):
        self.round_hp = self.round_hp+Hp
        self.Damage=self.Damage + Damage
    def temp_buff(self,Damage,Hp):
        print(Hp,Damage,"temp buff")
        self.round_hp = self.round_hp+Hp
        self.Damage=self.Damage + Damage
        self.temp_buff_hp = Hp
        self.temp_buff_damage= Damage
    def activation_condition(self,type):
        # print(self.Name)
        if type=="faint":
           
            if self.alive_check() == False:
                
                self.ability_flag= True

                

    def round_end(self):
        self.state = "Alive"
        self.activated_flag = False
        self.round_hp=self.base_Hp
        self.Damage=self.Damage-self.temp_buff_damage
        self.temp_buff_damage = 0
        self.temp_buff_hp = 0
class Board:
    def __init__(self,units):
        self.order = []
        self.start_order = []
        for unit in units:
            self.order.append(unit)
            self.start_order.append(unit)
    def show_order(self):
        for position,units in enumerate(self.order[::-1]):
            self.order.append(units)
            # print(position,units.Name, unitsround_hp, units.Damage)
    
    def amount_units(self):
        return len(self.order)
    def remove_fainted_list(self):
       
        
        self.order = [x for x in self.order if  x.alive_check()]
    
        # print(self.order[0].alive_check())



    def show_order_display(self,other_board = None):
        
        base_upper=" ---------"
        base_upo_middle = " |   P   |"
        base_middle = " |  N   |"
        base_low_middle = " |  d  h |"
        base_lower=" ---------"
        curr_upper=""
        curr_upo_middle = ""
        curr_middle = ""
        curr_low_middle = ""
        curr_lower=""
        for position,units in enumerate(self.order[::-1]):
            # self.order.append(units)
            # print(f""" -----{position}---\n|    {units.Name}    |\n|damage:{units.Damage}||hp:{unitsround_hp}|""")
            curr_upper=curr_upper+base_upper
            curr_upo_middle =curr_upo_middle+base_upo_middle.replace("P",str(position))
            curr_middle = curr_middle + base_middle.replace("N",units.Name[0:2])
            tmep_ =  base_low_middle.replace("d",str(units.Damage))
            tmep_ = tmep_.replace("h",str(units.round_hp))
            curr_low_middle = curr_low_middle + tmep_
            curr_lower=curr_lower+base_lower
        curr_upper= curr_upper+"          __    "
        curr_upo_middle=curr_upo_middle+"  /\   /\/ _\   "
        curr_middle=curr_middle+"  \ \ / /\ \    "
        curr_low_middle=curr_low_middle+"   \ V / _\ \   "
        curr_lower=curr_lower + "    \_/  \__/   "
        for position,units in enumerate(other_board.order):
            # self.order.append(units)
            # print(f""" -----{position}---\n|    {units.Name}    |\n|damage:{units.Damage}||hp:{units.Hp}|""")
            curr_upper=curr_upper+base_upper
            curr_upo_middle =curr_upo_middle+base_upo_middle.replace("P",str(position))
            curr_middle = curr_middle + base_middle.replace("N",units.Name[0:2])
            tmep_ =  base_low_middle.replace("d",str(units.Damage))
            tmep_ = tmep_.replace("h",str(units.round_hp))
            curr_low_middle = curr_low_middle + tmep_
            curr_lower=curr_lower+base_lower

        
        print(curr_upper)
        print(curr_upo_middle)
        print(curr_middle)         
        print(curr_low_middle)
        print(curr_lower)   
    def random_ally(self,num_ally):

        list_ally_index = np.randint(0,self.amount_units(),num_ally)
            
        return list_ally_index
        
    def random_ally_single(self):

        list_ally_index = np.random.randint(0,self.amount_units(),1)
            
        return self.order[list_ally_index[0]]
    def update_board(self):
        ###careful of order
        self.update_board_level_1()
        # print(self.start_order[0].ability_flag,"BASE START ORDER")
        self.start_order_abilities = [x for x in self.start_order if  x.ability_flag and not x.activated_flag ]
       
        for units in self.start_order_abilities:
            
            units.ability(units,self)

            units.activated_flag = True
            print(units.Name,"ability acitciated")  

    def update_board_level_1(self):
        ###first surface level check
     
       
        for units in self.start_order:
            
            units.update()


    def add_unit_attack_q(self,unit):
        pass
    # def moveup(self):
        # for unit in self.order:
        #     unit
    def reset_board(self,board2):
        for units in self.start_order+board2.start_order:
            units.round_end()
        self.order = self.start_order
        board2.order = board2.start_order
    def fainted(self):
        print( [x for x in self.start_order if not x.alive_check()])
        
def battle_phase(board1,board2):
    # print(board1.show_order(),board2.show_order())
    battle_finished = False
    round_count= 0
    # print("board 1")
    board1.show_order_display(board2)
   
    # print("board 2")
    # board2.show_order_display()
    # battle_phase(board1,board2)
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
        board1.update_board()
        board2.update_board()
        
        
        # board1.update()
        
        #post attack
        board1.remove_fainted_list()
        board2.remove_fainted_list()
        # board1.update_board()
        # board2.update_board()
        # results
        # print(board1.amount_units())
        # print(board2.amount_units())
        if board1.amount_units() == 0 and  board2.amount_units()!=0:
                print("board 2 wins")
                battle_finished = True
                board1.show_order_display(board2)
                # return ("Lost")
        elif board1.amount_units() != 0 and board2.amount_units()==0:
                print("board 1 wins")
                battle_finished = True
                board1.show_order_display(board2)
                # return ("Win")
            
        elif board1.amount_units() == 0 and board2.amount_units()==0:
                print("draw")
                battle_finished = True
                
                # return "draw"
        else:
                board1.show_order_display(board2)
                continue
        
        
    ##

    
dict_of_pets= {1:["duck","beaver","otter","pig","ant","mosqutio","rat","fish","cricket","horse"],3:["snail","crab","swan","rat","hedgehog","peacock","flmingo","worm","kangaroo","spider"],5:["dodo","badger","dolphin","giraffe","elephint","camel","rabbit","bull","dog","sheep"]
               ,7:["skunk","hipoo","pufferfish","turtle","squrial","penguin","deer","whale","parrot"],9:["scropion","crocidle","rhino","monkey","armadilo","cow","seal","chciken","shark","turkey"]
               ,11:["leopard","boar","tiger","wolvrine","gorilla","dragon","mamotth","cat","snake","fly"]}

class Unit_store:
    def __init__(self):
        self.amount_of_units=3
        self.units= []
        self.turn = 1
        self.gold = 10
    def increase_turn(self):
        self.turn=self.turn+1
        if self.turn ==5 or self.turn == 9:
            self.amount_of_units = self.amount_of_units+1

    def generate_units(self):
        generated_units = np.randint((self.turn-1//2)*10,self.amount_of_units)
            
        return generated_units
    def buy(self,unit,place):
        if self.gold >2:
            self.gold -3
            self.units.insert(unit,place)
        
def display_board(board1,board2):
    # while add loops here for gods sake 



    # print("board 1")
    # board1.show_order_display()
    
    # print("board 2")
    # board2.show_order_display()
    battle_phase(board1,board2)
    print("post battle")
    board1.reset_board(board2)
    print(board1.show_order_display(board2))
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
    

print(dict_of_pets[1]+dict_of_pets[3])

# ant= Unit("ant",2,3)
# ant1= Unit("otter",1,3)
# first_board = Board([ant,ant1])
# otter_buffed= Unit("duck",2,3)
# otter_buffed1= Unit("duck",2,3)
# otter_buffed2= Unit("duck",2,3)
# second_board = Board([otter_buffed,otter_buffed1,otter_buffed2])
# display_board(first_board,second_board)