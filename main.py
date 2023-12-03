# import tensorflow as tf
# import random


import unittest

### TODO:
#horse ability
#unit testing 
#Cricket ability 
#Items
#Apple
#Honey 
#level up
#convert rat and pig to beaver function
#check for attack order exactly
#convert units in a dictonary of abilties to states and see if that state in the lookup table 
from numpy.random import seed
from numpy.random import randint
import numpy as np
import copy 
# from pet_abilties import *
class match_env:
    def __init__(self):
        pass
    #turn is something adding up as a count 

def apple_ability(target,owener_board):
        ## Needs testing
        owener_board[target].perma_buff(1,1)

        
        print("apple ability worked")

    
# def board_cleanup(board1,board2):
#     board1
##stack order
#1)hurt (alive units get pirio)
#2)faint (by which one dies first) (tie is broken by left to right on player side?)


def otter_ability(otter,owner_board):

    for unit in owner_board.board.random_n_amount_of_units(otter.level):

        unit.perma_buff(0,1) 
    
    ##when bought give random ally +1*lvl hp 
        
def mosquito_ability(mosqiuto,owner_board):
   
        owner_board.order[owner_board.random_single_unit()].take_damage(mosqiuto.level)
      
 

        # owner_board = None
    

def ant_ability(self,owner_board=None):
   
        buff_amount = self.level
        owner_board.order[owner_board.random_single_unit()].temp_buff(buff_amount,buff_amount)
        

def rat_ability(self,owner_board):
    shop_board.append()
def duck_ability(duck,owner_board):
    
    for unit in owner_board.shop_units:
        unit.perma_buff(0,duck.level)
        print("duck buffed" ,unit.Name)


def beaver_ability(beaver,owner_board):
   for unit in owner_board.shop.shop_board.random_n_amount_of_units(2):

        unit.perma_buff(beaver.level,0) 
   
def cricket_ability(cricket,player_board):
    player_board.insert(0,Unit("zombiecircket",1,1))# add it at the start of line in combat 

def fish_ability(fish,player_board): 
       for unit in player_board.random_n_amount_of_units(2):

        unit.perma_buff(fish.level,fish.level)  

def skippper(self= None,skipper = None):
    return False



def start_of_battle(self):
    
    return  self.owner_board.state == "start_of_battle"

def level_up_activataction(self):
    pass # WIP
def summon_activation(self):
    pass #WIP
## has a list of summoned units that are check by the horse and are buffed by the horse 
status = ["buy,sell,faint,none,start_of_battle"]
ability_dict ={"ant":[ant_ability,"faint"],"otter":[otter_ability,"buy"],"mosqutio":[mosquito_ability,"start_of_battle"],
               "duck":[duck_ability,"sell"],"beaver":[beaver_ability,"sell"],"pig":[skippper,"none"],"mouse":[otter_ability,"buy"],
               "fish":[fish_ability,"none"],"cricket":[otter_ability,"buy"],"horse":[skippper,"buy"]} 

class Unit:
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.base_hp = Hp
      
        self.Base_damage = Damage
        # x.ability_flag and not x.activated_flag
        self.Cost =3 
        self.level=1
        self.Tier=1
        self.Sell_price=self.level
        self.perk = None
        self.level_amount = 0
        self.ability=ability_dict[Name][0]
        self.temp_buff_hp = 0
        self.temp_buff_damage= 0
        self.activated_flag = False
        self.owner_board = None
        self.ablity_game_state = ability_dict[Name][1]
        self.ability_limit=0
        self.ability_flag=False
        self.ability_used = False
        self.state = None
        self.alive = True

    def update_state(self,state):
        self.state = state
    def increase_level(self):
        self.level  ## WIP
    
    def dict_for_activation(self):
        # save this for when we try to find 
        return {self.ablity_game_state:self.ability}

    def update(self,owner_board):
        # update only makes the ability in que be ware of this
        #another object has to force the ability to activate 
        # print("update in progress")
        self.owner_board = owner_board
        # print(self.state)
        # print(self.ablity_game_state,self.state)
        if (self.state==self.ablity_game_state) and not self.ability_used:
            self.ability(self,self.owner_board) ## We must send the board to avoid any issues later on 
            self.ability_used = True
            # print("update worked")
    def attack(self,enemy):
        enemy.base_hp = enemy.base_hp - self.Base_damage
        self.base_hp = self.base_hp - enemy.Base_damage
        print(self.Name, " attacked ",enemy.Name )
        print(enemy.Name, " attacked ",self.Name )
        if enemy.base_hp <= 0:
            enemy.alive = False
        if self.base_hp <= 0:
            self.alive = False
    
    def alive_check(self):
        return self.alive
    def perma_buff(self,Damage,Hp):
        # print("perma_buffing")
        self.base_hp = self.base_hp+Hp
        self.Base_damage=self.Base_damage + Damage
    def temp_buff(self,Damage,Hp):
        # print(Hp,Damage,"temp buff")
        self.base_hp = self.base_hp+Hp
        self.Base_damage=self.Base_damage + Damage
        self.temp_buff_hp = self.temp_buff_hp+ Hp
        self.temp_buff_damage=self.temp_buff_damage +Damage
    # def activation_condition(self,function):
    #     # print(self.Name)
    #     # print(function(self),"function check")
        
    #     if function:
    #             self.ability_flag= True

        

    def round_end(self):
        self.alive = True
        self.activated_flag = False
        self.base_hp=self.base_hp - self.temp_buff_hp
        self.Base_damage=self.Base_damage-self.temp_buff_damage
        self.temp_buff_damage = 0
        self.temp_buff_hp = 0

    def take_damage(self,damage_amount):
        self.base_hp= self.base_hp -damage_amount
        if self.base_hp <= 0:
            self.alive = False

            
class Board:
    def __init__(self):
        self.order = []
        self.start_order = []
        self.board_state= None
        self.alive = True
        self.enemy_board = None
        self.shop = None
        self.targetable_units =[]
            # self.player_units= ["0","1","2","3","4"]##player units 
  
        self.position_unit_dict = {0:None,1:None,2:None,3:None,4:None}

    # def summon(self,unit):
    #     self.order.append(0,unit)
    #     for k in self.order(): 
    #         if ability_dict[k.Name][1]== "summon":# trying to activate all simmon ability and give them a target of the summoned unit 
    #             print()
    def swap_unit_place(self,origin,end):
             
             if self.position_unit_dict[end].Name  == self.position_unit_dict[origin].Name and not self.position_unit_dict[end].level == 3:
                # self.position_unit_dict[place].Name == self.shop_units[index].Name and not self.shop_units[index].level == 3:
                print("LEVELING UP ")
                self.position_unit_dict[end].level_amount = self.board.position_unit_dict[end].level_amount  +self.position_unit_dict[end] +1
                self.position_unit_dict[end].perma_buff(self.position_unit_dict[origin],self.position_unit_dict[end])

                if self.position_unit_dict[place].level == 1 and self.board.position_unit_dict[place].level_amount ==2 :
                    self.position_unit_dict[place].update_state("level_up")
                    self.position_unit_dict[place].update()
                    self.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1

                    self.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 4

                if self.position_unit_dict[place].level == 2 and self.board.position_unit_dict[place].level_amount >2:
                    self.position_unit_dict[place].update_state("level_up")
                    self.position_unit_dict[place].update()
                    self.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 3
                    self.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1

            
    def show_order(self):
        # for position,units in enumerate(self.order[::-1]):
        #     self.order.append(units)
            # print(position,units.Name, unitsround_hp, units.Base_damage)
        # print(self.order,"show order")
        # print(self.order[0])
        pass
    
    def amount_units(self):
        return len(self.order)
    def remove_fainted_list(self):
        temp_list = []
        for unit in self.order:
            
            if unit.alive_check():
                temp_list.append(unit)
            else:
                self.order.remove(unit)
                unit.update_state("faint")

                unit.update(self)
            # self.order = [x for x in self.order if  x.alive_check()]

       
        # print(self.order[0].alive_check())
    def total_of_hp_and_damage(self):
        total_hp =0 
        total_damage = 0
        
        for unit in self.order:
            
            print(unit.Name,unit.alive)
            total_hp =  total_hp +unit.base_hp 
            total_damage =  total_damage +unit.Base_damage ####### nOOOOOOOOOOOOOOOOOOOOOOOOOOOOONnnnnnnnnnnnnnnnnnnnnnnnn
        return [total_damage,total_hp]
    def total_of_hp_and_damage_prebattle(self):
        total_hp =0 
        total_damage = 0
        self.create_targetable_list()
        
        for unit in self.targetable_units:
            
            # print(unit.__dir__())
            total_hp =  total_hp +unit.base_hp 
            total_damage =  total_damage +unit.Base_damage ####### nOOOOOOOOOOOOOOOOOOOOOOOOOOOOONnnnnnnnnnnnnnnnnnnnnnnnn
        return [total_damage,total_hp]

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
            # print(f""" -----{position}---\n|    {units.Name}    |\n|damage:{units.Base_damage}||hp:{unitsround_hp}|""")
            curr_upper=curr_upper+base_upper
            curr_upo_middle =curr_upo_middle+base_upo_middle.replace("P",str(position))
           
            curr_middle = curr_middle + base_middle.replace("N",units.Name[0:2])
            tmep_ =  base_low_middle.replace("d",str(units.Base_damage))
            tmep_ = tmep_.replace("h",str(units.base_hp))
            curr_low_middle = curr_low_middle + tmep_
            curr_lower=curr_lower+base_lower
        curr_upper= curr_upper+"          __    "
        curr_upo_middle=curr_upo_middle+"  /\   /\/ _\   "
        curr_middle=curr_middle+"  \ \ / /\ \    "
        curr_low_middle=curr_low_middle+"   \ V / _\ \   "
        curr_lower=curr_lower + "    \_/  \__/   "
        for position,units in enumerate(other_board.order):
            # self.order.append(units)
            # print(f""" -----{position}---\n|    {units.Name}    |\n|damage:{units.Base_damage}||hp:{units.Hp}|""")
            curr_upper=curr_upper+base_upper
            curr_upo_middle =curr_upo_middle+base_upo_middle.replace("P",str(position))
            curr_middle = curr_middle + base_middle.replace("N",units.Name[0:2])
            tmep_ =  base_low_middle.replace("d",str(units.Base_damage))
            tmep_ = tmep_.replace("h",str(units.base_hp))
            curr_low_middle = curr_low_middle + tmep_
            curr_lower=curr_lower+base_lower

        
        print(curr_upper)
        print(curr_upo_middle)
        print(curr_middle)         
        print(curr_low_middle)
        print(curr_lower)   
    
    def random_n_amount_of_units(self,num_ally):
        self.create_targetable_list()
        # print(num_ally,len(self.targetable_units),"num ally and len targetable")
        if len(self.targetable_units) != 0:
       
          
        
          list_ally_index = np.random.choice(self.targetable_units, size=num_ally, replace=False)
 
          temp_list = []
        
          for k in list_ally_index:
                
                 temp_list.append(k)
          return temp_list
        else:
          return []
    
    def random_single_unit(self):

        list_ally_index = np.random.randint(0,self.amount_units(),1) ## check this if a single random unit is being called and acts funny not using np methods of others 

        print(list_ally_index,"ally_list Index")
       
        return list_ally_index[0]
    def update_board(self):
 
 
        for unit in self.order:
            unit.update_state("mid_battle")
            unit.update(self)
            


    def start_of_battle_for_units(self):
        for unit in self.order:
            unit.update_state("start_of_battle")
            unit.update(self)
    def add_unit_attack_q(self,unit):
        pass
    def shop_linking(self,shop):    
        self.shop = shop
    def reset_board(self,board2):
        for units in self.start_order+board2.start_order:
            units.round_end()
        self.order = self.start_order
        board2.order = board2.start_order
    def fainted(self):
        print( [x for x in self.start_order if not x.alive_check()])
    # def start_board(self,board2):
    #     self.board_state = "start_of_battle"
    #     board2.board_state = "start_of_battle"
    def mid_battle_state(self,board2):
        self.board_state = "mid_battle"
        board2.board_state = "mid_battle"
    def enemy_board_linking(self,board2):
        self.enemy_board =board2
        board2.enemy_board = self
    def create_targetable_list(self):
        self.targetable_units =[]
        for units in self.position_unit_dict.values(): 
          
            
            if units != None:
             
                self.targetable_units.append(units)
    
    def create_board_for_battle(self):
        # process list   
        list_for_battle = self.position_unit_dict.values()
        # print(list_for_battle,"list for battle")
        temp_ = []
        for elemnt in list_for_battle:
                if elemnt != None:
                    temp_.append(elemnt)         

        
        self.order = copy.deepcopy(temp_)
def battle_phase(board1,board2,round_num = None):
    # print(board1.show_order(),board2.show_order())
    battle_finished = False
    round_count= 0
    # print("board 1")
    board1.show_order_display(board2)
    board1.enemy_board_linking(board2)
    board1.create_board_for_battle()
    board2.create_board_for_battle()
    # print(board1.total_of_hp_and_damage(),"total hp limit")
    # print("board 2")
    # board2.show_order_display()
    # battle_phase(board1,board2)
    if round_num == None:
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
                board1.show_order_display(board2)
                board1.start_of_battle_for_units()
                board2.start_of_battle_for_units()
                print("START THE ROUND")
              
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
    else:
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
              
                # board1.show_order_display(board2)
                board1.show_order_display(board2)
                board1.start_of_battle_for_units()
                board2.start_of_battle_for_units()
                print("START THE ROUND")
             
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
        
            if round_count == round_num:
                return board1.total_of_hp_and_damage()      

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

dict_of_pets_with_stats ={"duck":Unit("duck",2,3),"beaver":Unit("beaver",3,2),"otter":Unit("otter",1,3),"pig":Unit("pig",4,1),"ant":Unit("ant",2,2),"mosqutio":Unit("mosqutio",2,2),
                          "mouse":Unit("mouse",1,2),"fish":Unit("fish",2,3),"cricket":Unit("cricket",1,2),"horse":Unit("horse",2,1)}
dict_of_items={1:["apple","honey"],3:["pill","meat","cupcake"],5:["salad","onion"],7:["canned food","pear"],9:["pepper","choco","sushi"],11:["steak","melon","mushroom","pizza"]}
class Unit_store:
    def __init__(self):
        self.amount_of_units=3
        self.units_pool= np.array([])
        self.turn = 1
        self.gold = 10
        
        self.shop_units=list()
        self.add_unitpool()
        self.temp_shop = []
        self.targetable_units =[]
        self.freeze_list = []
        self.board = None
    def increase_turn(self):
        self.turn=self.turn+1
        if self.turn ==5 or self.turn == 9:
            self.amount_of_units = self.amount_of_units+1
        if self.turn in [3,7,9,11]:
            self.add_unitpool()
    def link_to_board(self,board):
        self.board = board

                # print(self.targetable_units,"self adding")
        # print(self.targetable_units,"self targetable finish")
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
        generated_units = np.random.randint((self.turn-1//2)*10,size=self.amount_of_units-len(self.freeze_list))
        self.temp_shop = []
        
        

        self.shop_units=self.units_pool[generated_units]
       
        for unit in self.shop_units:                      
            
            new_unit = dict_of_pets_with_stats[unit]
          
            
            # self.shop_units = np.insert(self.player_units,index,new_unit)
            
            self.temp_shop.append(new_unit)
           
            # self.shop_units= np.delete(self.shop_units,index)
            # np.delete(self.shop_units,index)
            # self.player_units = np.insert(self.player_units,index,new_unit)
        self.shop_units = copy.deepcopy(self.temp_shop)
        for units in self.freeze_list:
            self.shop_units.append(units)
        
        self.temp_shop=[]#empty to avoid memory issues 
   

        # print(self.shop_units,"shop units")
    def buy(self,index,place):
        
        if self.board.position_unit_dict[place] == None:
                
            if self.gold >2:
                self.gold =self.gold-3
                

                #bought effects
                # self.shop_units[index].bought = True
                self.shop_units[index].update_state("buy")
                self.shop_units[index].owner_board = self.board
                self.shop_units[index].update(self)

               
                self.board.position_unit_dict[place]= self.shop_units[index]
                
                   

                # np.insert( self.player_units,place,self.shop_units[index]) 
                # print(self.shop_units[index],"shop unit index")

                self.shop_units= np.delete(self.shop_units,index) 
                # print("bought the ",self.shop_units[0].Name,place,"bought test")
        elif  self.board.position_unit_dict[place].Name == self.shop_units[index].Name and not self.shop_units[index].level == 3:
             print("LEVELING UP ")
             self.board.position_unit_dict[place].level_amount = self.board.position_unit_dict[place].level_amount  +self.shop_units[index].level +1
             self.board.position_unit_dict[place].perma_buff(self.shop_units[index].level,self.shop_units[index].level)

             if self.board.position_unit_dict[place].level == 1 and self.board.position_unit_dict[place].level_amount ==2 :
                 self.board.position_unit_dict[place].update_state("level_up")
                 self.board.position_unit_dict[place].update()
                 self.board.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1

                 self.board.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 4

             if self.board.position_unit_dict[place].level == 2 and self.board.position_unit_dict[place].level_amount >2:
                 self.board.position_unit_dict[place].update_state("level_up")
                 self.board.position_unit_dict[place].update()
                 self.board.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 3
                 self.board.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1
        else:
             print("UNIT IS ALREADY IN THAT PLACE")
    
    def add_unitpool(self):
        self.units_pool=  np.concatenate((self.units_pool,dict_of_pets[self.turn]))
        # np.concatenate([a,b], axis=1) 
    def reroll(self):
        if self.gold >0:
            ##TODO Add the sliding affect when the shop clips
            self.generate_units()
            self.gold = self.gold-1
        else:
            print(self.gold)
 
    def read(self):
        for k in self.shop_units:
         
                print(k.Name,k.Base_damage,k.base_hp)
        # print(self.shop_units,"SHOW READ IS ")
    def read_player_units(self):
        for ind,k in enumerate(self.board.position_unit_dict.values()):
            if isinstance(k,Unit):
                print(ind,k.Name,k.Base_damage,k.base_hp)

    def shop_units(self):
        print(self.shop_units)
    def selling(self,index):
        # self.board.player_units
        # sold units get a free pass and quickly get their abilities activated rather than having to call the long ability process.
        print(self.board.position_unit_dict[index],"selling is given this to sell") ## make sure to see things 
        if isinstance(self.board.position_unit_dict[index],Unit):
            if self.board.position_unit_dict[index].Name == "pig": ## just use the normal function
                self.gold= self.gold + self.board.position_unit_dict[index].level
            self.gold= self.gold + self.board.position_unit_dict[index].level  
            print(self.board.position_unit_dict[index].Name,"unit being sold")
            self.board.position_unit_dict[index].update_state("sell")
            self.board.position_unit_dict[index].update(self)
            self.board.position_unit_dict[index] = None
                       
    def freeze(self,index):
        self.freeze_list.append(self.shop_units[index])      
    def unfreeze(self,index):
      
        if index <= len(self.freeze_list):
            self.freeze_list.pop(index)
          
        else:
            print("can't unfreeze anything")
    def amount_units(self):
        temp_num = 0
        for units in self.player_units:

            if not isinstance(units,str):
                temp_num = temp_num +1

        return temp_num
    def gold_check(self):
        print(f"player gold is : {self.gold}")
    
class Item_shop:
    ## add freezing, refreshing, generating 
    def __init__(self,unit_store):
        self.linked_shop = unit_store
        
        self.turn = unit_store.turn # might cause issues 
        self.item_pool = np.array([])
        self.item_list=list()
        self.amount_of_items = 2 
        self.add_item_pool()
        self.temp_shop = []
  
    def increase_turn(self):
        self.turn=self.turn+1
        if self.turn ==5 or self.turn == 9:
            self.amount_of_items = self.amount_of_items+1
        if self.turn in [3,7,9,11]:
            self.add_item_pool()

    def add_item_pool(self):
        self.item_pool=  np.concatenate((self.item_pool,dict_of_items[self.turn]))
        
    def generate_items(self):
        generated_units = np.random.randint((self.turn-1//2)*10,size=self.amount_of_items)
        self.temp_shop = []
        
        
        self.item_list=self.item_pool[generated_units]
       
        for unit in self.shop_units:                      
            
            new_unit = dict_of_pets_with_stats[unit]
          
            
            # self.shop_units = np.insert(self.player_units,index,new_unit)
            
            self.temp_shop.append(new_unit)
           
            # self.shop_units= np.delete(self.shop_units,index)
            # np.delete(self.shop_units,index)
            # self.player_units = np.insert(self.player_units,index,new_unit)
        self.shop_units = copy.deepcopy(self.temp_shop)
        self.temp_shop=[]#empty to avoid memory issues 

    def reroll(self):
        ## only called from it's parent shop (hopefully)
        if self.gold >0:

            self.generate_items()
            
        else:
            print(self.gold)

dict_of_items_ability = {}
dict_of_items_types= {} 

class Item: # becareful there are many types of abiltiies from buffs to reducing damage once 
    ## link to the player unit board
    def __init__(self,name):
        self.name = name
        self.ability = dict_of_items_ability[name]
        self.type =  dict_of_items_types[name]
        self.cost = 3
    def change_cost(self,new_cost):
        self.cost = new_cost

    def use_ability(self,target):
        self.ability(shop_board[target])
    
        

        
# def display_board(board1,board2):
    # while add loops here for gods sake 



    # print("board 1")
    # board1.show_order_display()
    
    # print("board 2")
    # board2.show_order_display()   
    # battle_phase(board1,board2)
    
   
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
    

# battle_phase(board1,board2)
# board = Board()
# shop= Unit_store()
# board.shop_linking(shop)
# shop.link_to_board(board)
# shop.generate_units()
# # shop.reroll()
# shop.edit_shop([["pig",1,1],["pig",1,1],["mosqutio",1,1]])
# shop.read_player_units()

# ##buying removes the unit so it doesn't work if we buy in a certain order


# shop.buy(0,4)

# shop.buy(1,1)

# shop.buy(0,3)   
# print("read players units")

board = Board()
shop= Unit_store()
board.shop_linking(shop)
shop.link_to_board(board)
shop.generate_units()
# shop.reroll()
shop.edit_shop([["pig",1,1],["pig",1,1],["pig",1,1]])
shop.buy(0,4)
shop.buy(1,4)
shop.buy(0,4)   
print(board.position_unit_dict[4].Name,board.position_unit_dict[4].level,board.position_unit_dict[4].level_amount)
# total_hp =battle_phase(board,board, 1) 

# print(total_hp,"total hp_")




# shop.selling(1)

# print("sold the beaver units")
# shop.read_player_units()

# battle_phase(board,board,1)

# display_board(board,board)





# shop= Unit_store()
# shop.generate_units()
# # shop.reroll()
# shop.edit_shop([["otter",1,1],["otter",1,1],["otter",1,1]])
# shop.read_player_units()

##buying removes the unit so it doesn't work if we buy in a certain order

class CustomTests(unittest.TestCase):
    def test_otter_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        shop.edit_shop([["otter",1,1],["otter",1,1],["otter",1,1]])
        shop.read_player_units()
        shop.buy(0,4)
        shop.buy(1,2)
        shop.buy(0,1)    
        shop.read_player_units()
        self.assertEqual(board.total_of_hp_and_damage_prebattle(),[3,5],"Otter test failed")

    def test_duck_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        shop.edit_shop([["pig",1,1],["pig",1,1],["duck",1,1]])
                # shop.read_player_units()
                
        shop.buy(2,4)
        shop.selling(4)
        shop.buy(1,2)
        shop.buy(0,1)    
        # shop.read_player_units()
        #start combat here ? and take the hp total during round 1?
        total_hp =battle_phase(board,board,1) 
        self.assertEqual(board.total_of_hp_and_damage_prebattle(),[2,4],"Duck test failed")


    def test_mosqutio_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["mosqutio",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        total_hp =battle_phase(board,board, 1) 
        self.assertEqual(total_hp,[1,1],"Mosqutio test failed")

    def test_ant_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["ant",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        total_hp =battle_phase(board,board, 1) 
        self.assertEqual(total_hp,[3,3],"Ant test failed")

# unittest.main() 

# board_for_combat.show_order_display(board_for_combat)
# display_board(board_for_combat,board_for_combat)
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



### units[state] <- if state === abuluty _