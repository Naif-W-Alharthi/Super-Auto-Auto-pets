# import tensorflow as tf
# import random
from numpy.random import seed
from numpy.random import randint
import numpy as np
import copy 
class match_env:
    def __init__(self):
        pass
    #turn is something adding up as a count 


def otter_ability(otter,owner_board):
    
    for k in owner_board.random_n_amount_of_units(otter.level):
        print(k.base_Hp,k.Damage)
        k.perma_buff(1,0) 
        print("buffed", k.Name)
        print(k.base_Hp,k.Damage)
    ##when bought give random ally +1*lvl hp 
    
def mosquito_ability(self,owner_board):
    print("MOSQUITO ACTIVE ")
    if self.ability_flag == True:
        target_unit =owner_board.enemy_board.random_single_unit()
        target_unit.take_damage(self.level)
        print(target_unit.Name, "took damage")
        owner_board.enemy_board.remove_fainted_list()
        owner_board.remove_fainted_list()
    

def ant_ability(self,owner_board=None):
    if self.ability_flag == True:
        buff_amount = self.level
        self.owner_board.random_single_unit().temp_buff(buff_amount,buff_amount)
        


def duck_ability(duck,shop_board):
    pass
    
# def board_cleanup(board1,board2):
#     board1
##stack order
#1)hurt (alive units get pirio)
#2)faint (by which one dies first) (tie is broken by left to right on player side?)
#

def buy_activiation(self):
    return self.bought
def faint_activation(self):
    return not self.alive_check()
    
def skippper(self):
    return False

def start_of_battle(self):
    
    return  self.owner_board.state == "start_of_battle"

ability_dict ={"ant":[ant_ability,"faint"],"otter":[otter_ability,"buy"],"mosqutio":[mosquito_ability,"start_of_battle"],
               "duck":[otter_ability,"buy"],"beaver":[otter_ability,"buy"],"pig":[otter_ability,"buy"],"mouse":[otter_ability,"buy"],
               "fish":[otter_ability,"buy"],"cricket":[otter_ability,"buy"],"horse":[otter_ability,"buy"]} 
ability_type_dict= {"faint":faint_activation,"buy":buy_activiation,"start_of_battle":start_of_battle}
class Unit:
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.round_hp = Hp
        self.base_Hp = Hp
        self.Damage = Damage
        # x.ability_flag and not x.activated_flag
        self.Cost =3 
        self.level=1
        self.Tier=1
        self.Sell_price=self.level
        self.perk = None
        self.state="Alive"
        self.ability=ability_dict[Name][0]
        self.temp_buff_hp = 0
        self.temp_buff_damage= 0
        self.activated_flag = False
        self.owner_board = None
        self.ability_condtion_func = ability_type_dict[ability_dict[Name][1]]
        self.ability_limit=0
        self.ability_flag=False
        self.bought =False

    def update(self):
        # print(self.activation_condition_var)
     
        self.activation_condition(self.ability_condtion_func(self))
    def attack(self,enemy):
        enemy.round_hp = enemy.round_hp - self.Damage
        self.round_hp = self.round_hp - enemy.Damage
        print(self.Name, " attacked ",enemy.Name )
        print(enemy.Name, " attacked ",self.Name )
        if enemy.round_hp <= 0:
            enemy.state="Faint"
        if self.round_hp <= 0:
            self.state="Faint"

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
    def activation_condition(self,function):
        # print(self.Name)
        # print(function(self),"function check")
        
        if function:
           
           
                
                self.ability_flag= True

                

    def round_end(self):
        self.state = "Alive"
        self.activated_flag = False
        self.round_hp=self.base_Hp
        self.Damage=self.Damage-self.temp_buff_damage
        self.temp_buff_damage = 0
        self.temp_buff_hp = 0

    def take_damage(self,damage_amount):
        self.round_hp= self.round_hp -damage_amount
class Board:
    def __init__(self,units):
        self.order = []
        self.start_order = []
        self.state= None
        self.enemy_board = None
        for unit in units:
            self.order.append(unit)
            self.start_order.append(unit)
            unit.owner_board = self
    def add_unit(self,unit):
        self.start_order= self.start_order.append(unit)
    
    def show_order(self):
        # for position,units in enumerate(self.order[::-1]):
        #     self.order.append(units)
            # print(position,units.Name, unitsround_hp, units.Damage)
        print(self.order,"show order")
        print(self.order[0])
    
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
    def random_n_amount_of_units(self,num_ally):

        list_ally_index = np.random.randint(0,self.amount_units(),num_ally)
        print(list_ally_index,"list ally_dindex")
        temp_list = []
        for k in list_ally_index:
                temp_list.append(self.order[k])
        return temp_list
        
    def random_single_unit(self):

        list_ally_index = np.random.randint(0,self.amount_units(),1)
        
        return self.order[list_ally_index[0]]
    def update_board(self):
        ###careful of order
        self.update_board_level_1()
        # print(self.start_order[0].ability_flag,"BASE START ORDER")
        self.start_order_abilities = [x for x in self.start_order if  x.ability_flag and not x.activated_flag ]
        print(self.start_order_abilities)
        for units in self.start_order_abilities:
            print(units,"ability and unity",units.ability)
            units.ability(units,self)

            units.activated_flag = True
            print(units.Name,"ABILITY FOR THE UNIT HAVE USE222")  
    def update_board_level_1(self):
        ###first surface level check
        for units in self.start_order:      
            units.update()

    def add_unit_attack_q(self,unit):
        pass

    def reset_board(self,board2):
        for units in self.start_order+board2.start_order:
            units.round_end()
        self.order = self.start_order
        board2.order = board2.start_order
    def fainted(self):
        print( [x for x in self.start_order if not x.alive_check()])
    def start_board(self,board2):
        self.state = "start_of_battle"
        board2.state = "start_of_battle"
    def mid_battle_state(self,board2):
        self.state = "mid_battle"
        board2.state = "mid_battle"
    def enemy_board_linking(self,board2):
        self.enemy_board =board2
        board2.enemy_board = self
def battle_phase(board1,board2):
    # print(board1.show_order(),board2.show_order())
    battle_finished = False
    round_count= 0
    # print("board 1")
    board1.show_order_display(board2)
    board1.enemy_board_linking(board2)
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
        if round_count ==1:
            print("START THE ROUND")
            board1.start_board(board2)
            board1.remove_fainted_list()
            board2.remove_fainted_list()
        else:
            board1.mid_battle_state(board2)
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

    
dict_of_pets= {1:["duck","beaver","otter","pig","ant","mosqutio","mouse","fish","cricket","horse"],3:["snail","crab","swan","rat","hedgehog","peacock","flmingo","worm","kangaroo","spider"],5:["dodo","badger","dolphin","giraffe","elephint","camel","rabbit","bull","dog","sheep"]
               ,7:["skunk","hipoo","pufferfish","turtle","squrial","penguin","deer","whale","parrot"],9:["scropion","crocidle","rhino","monkey","armadilo","cow","seal","chciken","shark","turkey"]
               ,11:["leopard","boar","tiger","wolvrine","gorilla","dragon","mamotth","cat","snake","fly"]}

dict_of_pets_with_stats ={"duck":[2,3],"beaver":[3,2],"otter":[1,3],"pig":[4,1],"ant":[2,2],"mosqutio":[2,2],"mouse":[1,2],"fish":[2,3],"cricket":[1,2],"horse":[2,1]}
dict_of_items={1:["apple","honey"],3:["pill","meat","cupcake"],5:["salad","onion"],7:["canned food","pear"],9:["pepper","choco","sushi"],11:["steak","melon","mushroom","pizza"]}
class Unit_store:
    def __init__(self):
        self.amount_of_units=3
        self.units_pool= np.array([])
        self.turn = 1
        self.gold = 10
        self.player_units= ["0","1","2","3","4","5","6"]##player units 
        self.shop_units=list()
        self.add_unitpool()
        self.temp_shop = []
    def increase_turn(self):
        self.turn=self.turn+1
        if self.turn ==5 or self.turn == 9:
            self.amount_of_units = self.amount_of_units+1
        if self.turn in [3,7,9,11]:
            self.add_unitpool()

      
            
    def edit_shop(self,shop):
        self.temp_shop = []
        self.shop_units =  shop
        for unit,damage,hp in shop:
            # damage,hp  = dict_of_pets_with_stats[unit]
            new_unit = Unit(unit,damage,hp)
          
            
            # self.shop_units = np.insert(self.player_units,index,new_unit)
            
            self.temp_shop.append(new_unit)
           
            # self.shop_units= np.delete(self.shop_units,index)
            # np.delete(self.shop_units,index)
            # self.player_units = np.insert(self.player_units,index,new_unit)
        self.shop_units = copy.deepcopy(self.temp_shop)
        self.temp_shop = []
    def generate_units(self):
        generated_units = np.random.randint((self.turn-1//2)*10,size=self.amount_of_units)
        self.temp_shop = []
        
        
        self.shop_units=self.units_pool[generated_units]
        
        for unit in self.shop_units:
            damage,hp  = dict_of_pets_with_stats[unit]
            new_unit = Unit(unit,damage,hp)
          
            
            # self.shop_units = np.insert(self.player_units,index,new_unit)
            
            self.temp_shop.append(new_unit)
           
            # self.shop_units= np.delete(self.shop_units,index)
            # np.delete(self.shop_units,index)
            # self.player_units = np.insert(self.player_units,index,new_unit)
        self.shop_units = copy.deepcopy(self.temp_shop)
        self.temp_shop=[]#empty to avoid memory issues 
   

        # print(self.shop_units,"shop units")
    def buy(self,index,place):
        print(self.shop_units,"SHOP SAW THIS LIST")
        
        if self.gold >2:
            self.gold =self.gold-3
            

            #bought effects
            self.shop_units[index].bought = True
            self.shop_units[index].update()
            
            
                

            self.player_units[place]= self.shop_units[index]

            # np.insert( self.player_units,place,self.shop_units[index]) 
            # print(self.shop_units[index],"shop unit index")
      
            self.shop_units= np.delete(self.shop_units,index)
            # print("bought the ",self.shop_units[0].Name,place,"bought test")
    def add_unitpool(self):
        self.units_pool=  np.concatenate((self.units_pool,dict_of_pets[self.turn]))
        # np.concatenate([a,b], axis=1) 
    def reroll(self):
        if self.gold >0:

            self.generate_units()
            self.gold = self.gold-1
        else:
            print(self.gold)
    def read(self):
        print(self.shop_units,"SHOW READ IS ")
    def read_player_units(self):
        print(self.player_units)
    def create_board_for_battle(self):
        # process list   
        for elemnt in ["0","1","2","3","4","5","6"]:
                if elemnt in self.player_units:
                    self.player_units.remove(elemnt)               
        print("PRE BOARD CREATION")
        for k in self.player_units:
            print(k.Name)           
            k.bought = False
        return self.player_units
    def freeze(self,index):
        # freeze unit
        pass
def display_board(board1,board2):
    # while add loops here for gods sake 



    # print("board 1")
    # board1.show_order_display()
    
    # print("board 2")
    # board2.show_order_display()
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
    

shop= Unit_store()
shop.generate_units()
# shop.reroll()
shop.edit_shop([["horse",1,1],["otter",1,1],["otter",1,1]])
shop.read()
shop.buy(0,1)
shop.buy(1,4)
# shop.buy(0,3)

# print("read players units")

board_for_combat = Board(shop.create_board_for_battle())
board_for_combat.show_order()
display_board(board_for_combat,board_for_combat)
# print(dict_of_pets[1]+dict_of_pets[3])

# ant= Unit("ant",0,3)
# ant1= Unit("mosqutio",0,3)
# first_board = Board([ant,ant1])
# otter_buffed= Unit("duck",2,3)
# # otter_buffed1= Unit("duck",2,3)
# # otter_buffed2= Unit("duck",2,3)
# second_board = Board([otter_buffed])
# display_board(first_board,second_board)

#pytorch
