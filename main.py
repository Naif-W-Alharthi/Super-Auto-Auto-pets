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
from numpy.random import seed
from numpy.random import randint
import numpy as np
import copy 
from pet_abilties import *
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



def buy_activiation(self):
    return self.bought
def faint_activation(self):
    return not self.alive_check()
    
def skippper(self= None,skipper = None):
    return False


def sell_activiation(self):
    print("checking on sell", self.selling)
    print((self.selling == True)," sell check is ")
    return (self.selling == True)

def start_of_battle(self):
    
    return  self.owner_board.state == "start_of_battle"

def level_up_activataction(self):
    pass # WIP
def summon_activation(self):
    pass #WIP
## has a list of summoned units that are check by the horse and are buffed by the horse 

ability_dict ={"ant":[ant_ability,"faint"],"otter":[otter_ability,"buy"],"mosqutio":[mosquito_ability,"start_of_battle"],
               "duck":[duck_ability,"sell"],"beaver":[beaver_ability,"sell"],"pig":[skippper,"none"],"mouse":[otter_ability,"buy"],
               "fish":[fish_ability,"none"],"cricket":[otter_ability,"buy"],"horse":[skippper,"buy"]} 
ability_type_dict= {"faint":faint_activation,"buy":buy_activiation,"start_of_battle":start_of_battle,"sell":sell_activiation,"summon":summon_activation,"none":skippper,}
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
        self.selling = False
        self.state = None
    def increase_level(self):
        self.level

    def update(self):
        # update only makes the ability in que be ware of this
        #another object has to force the ability to activate 
        
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
        # print("perma_buffing")
        self.round_hp = self.round_hp+Hp
        self.Damage=self.Damage + Damage
    def temp_buff(self,Damage,Hp):
        print(Hp,Damage,"temp buff")
        self.round_hp = self.round_hp+Hp
        self.Damage=self.Damage + Damage
        self.temp_buff_hp = self.temp_buff_hp+ Hp
        self.temp_buff_damage=self.temp_buff_damage +Damage
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
    def summon(self,unit):
        self.order.append(0,unit)
        for k in self.order(): 
            if ability_dict[k.Name][1]== "summon":# trying to activate all simmon ability and give them a target of the summoned unit 
                print()
    def show_order(self):
        # for position,units in enumerate(self.order[::-1]):
        #     self.order.append(units)
            # print(position,units.Name, unitsround_hp, units.Damage)
        # print(self.order,"show order")
        # print(self.order[0])
        pass
    
    def amount_units(self):
        return len(self.order)
    def remove_fainted_list(self):
       
        
        self.order = [x for x in self.order if  x.alive_check()]
    
        # print(self.order[0].alive_check())
    def total_of_hp_and_damage(self):
        total_hp =0 
        total_damage = 0
        for unit in self.order:
            # print(unit.__dir__())
            total_hp =  total_hp +unit.round_hp 
            total_damage =  total_damage +unit.Damage
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
        amount_of_targetable_allies = self.amount_units()

        list_ally_index = list_ally_index = np.random.choice(amount_of_targetable_allies, size=num_ally, replace=False)
        print(list_ally_index,"list ally_dindex")
        temp_list = []
        for k in list_ally_index:
                temp_list.append(self.order[k])
        return temp_list
        
    def random_single_unit(self):

        list_ally_index = np.random.randint(0,self.amount_units(),1) ## check this if a single random unit is being called and acts funny not using np methods of others 
        
        return self.order[list_ally_index[0]]
    def update_board(self):
        ###careful of order
        self.update_board_level_1()
        # print(self.start_order[0].ability_flag,"BASE START ORDER")
        self.start_order_abilities = [x for x in self.start_order if  x.ability_flag and not x.activated_flag ]
        print(self.start_order_abilities)
        for units in self.start_order_abilities:

            print(units,"ability and unity",units.ability)
            if units.ability_flag == True:
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

dict_of_pets_with_stats ={"duck":Unit("duck",2,3),"beaver":Unit("beaver",3,2),"otter":Unit("otter",1,3),"pig":Unit("pig",4,1),"ant":Unit("ant",2,2),"mosqutio":Unit("mosqutio",2,2),
                          "mouse":Unit("mouse",1,2),"fish":Unit("fish",2,3),"cricket":Unit("cricket",1,2),"horse":Unit("horse",2,1)}
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
        self.targetable_units =[]
        self.freeze_list = []
    def increase_turn(self):
        self.turn=self.turn+1
        if self.turn ==5 or self.turn == 9:
            self.amount_of_units = self.amount_of_units+1
        if self.turn in [3,7,9,11]:
            self.add_unitpool()

    def create_targetable_list(self):
        self.targetable_units =[]
        for units in self.player_units: 
            # print(units,"unit chcker")
            
            if not isinstance(units,str):
             
                self.targetable_units.append(units)
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
        
        
        if self.gold >2:
            self.gold =self.gold-3
            

            #bought effects
            self.shop_units[index].bought = True
            self.shop_units[index].update()
   
            self.shop_units[index].ability(self.shop_units[index],self) 
            self.shop_units[index].activated_flag = True
           
            
                

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
            ##TODO Add the sliding affect when the shop clips
            self.generate_units()
            self.gold = self.gold-1
        else:
            print(self.gold)
 
    def read(self):
        for k in self.shop_units:
         
                print(k.Name,k.Damage,k.round_hp)
        # print(self.shop_units,"SHOW READ IS ")
    def read_player_units(self):
        for ind,k in enumerate(self.player_units):
            if isinstance(k,Unit):
                print(ind,k.Name,k.Damage,k.round_hp)
    def create_board_for_battle(self):
        # process list   
        for elemnt in ["0","1","2","3","4","5","6"]:
                if elemnt in self.player_units:
                    self.player_units.remove(elemnt)               

        for k in self.player_units:
            # print(k.Name)           
            k.bought = False
        return self.player_units
    def shop_units(self):
        print(self.shop_units)
    def selling(self,index):
        # sold units get a free pass and quickly get their abilities activated rather than having to call the long ability process.
        print(self.player_units[index],"selling is given this to sell") ## make sure to see things 
        if isinstance(self.player_units[index],Unit):
            if self.player_units[index].Name == "pig": ## or RAT to add a free apple for user 
                self.gold= self.gold + self.player_units[index].level
            self.gold= self.gold + self.player_units[index].level  
            print(self.player_units[index].Name,"unit being sold")
            self.player_units[index].selling = True
            self.player_units[index].update()
         
            self.player_units[index].ability(self.player_units[index],self) 
            self.player_units[index].activated_flag = True
       
         
           
            print(len(self.player_units)," len of things before sell")
            self.player_units.pop(index)
            print(self.player_units,"player unit checker 200000")
            self.player_units.insert(index,str(index))
            print(self.player_units,"player unit checker 200000")
            print(len(self.player_units),"len of things after sell")                                      
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
shop.edit_shop([["otter",1,1],["otter",1,1],["otter",1,1]])
shop.read_player_units()

##buying removes the unit so it doesn't work if we buy in a certain order


shop.buy(0,4)

shop.buy(1,2)

shop.buy(0,1)   
# print("read players units")

# shop.selling(1)

# print("sold the beaver units")
shop.read_player_units()
board_for_combat = Board(shop.create_board_for_battle())
board_for_combat.show_order()
print(board_for_combat.total_of_hp_and_damage(),"HP and Damage")
# display_board(board_for_combat,board_for_combat)





# shop= Unit_store()
# shop.generate_units()
# # shop.reroll()
# shop.edit_shop([["otter",1,1],["otter",1,1],["otter",1,1]])
# shop.read_player_units()

##buying removes the unit so it doesn't work if we buy in a certain order

class CustomTests(unittest.TestCase):
    def test_otter_ability(self):
        shop= Unit_store()
        shop.generate_units()
        # shop.reroll()
        shop.edit_shop([["otter",1,1],["otter",1,1],["otter",1,1]])
        shop.buy(0,4)

        shop.buy(1,2)

        shop.buy(0,1)   
        # print("read players units")

        # shop.selling(1)

        # print("sold the beaver units")
        # shop.read_player_units()
        board_for_combat = Board(shop.create_board_for_battle())
        # board_for_combat.show_order()
        
        self.assertEqual(board_for_combat.total_of_hp_and_damage(),[3,5],"Otter test failed")

unittest.main()

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
