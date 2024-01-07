# import tensorflow as tf
# import random


import unittest

### TODO:
#we activate summoning using a function for now consider finding an efficent way to do this ?
#add pill
# add spider
#inserting should respect the max allowed units
from numpy.random import seed
from numpy.random import randint
import numpy as np
import copy 
# from pet_abilties import *
class match_env:
    def __init__(self):
        pass
    #turn is something adding up as a count 



    
# def board_cleanup(board1,board2):
#     board1

##stack order
#1)hurt (alive units get pirio)
#2)faint (by which one dies first) (tie is broken by left to right on player side?)
# ### TODO perma buffs aren't removed when adding units 
def swan_ability(swan,board,prior_list=None):
    board.shop.gold = board.shop.gold + swan.ability_level
def crab_ability(crab,board,prior_list=None):
    highest_hp = -2
    for unit in board.order:
        if unit != crab:
                if unit.base_hp> highest_hp:
                    highest_hp = unit.base_hp * (0.5*crab.ability_level)

    crab.base_hp = highest_hp
def snail_ability(snail,board,prior_list=None):
        if board.last_round_lost:
            for target in board.position_unit_dict.values():
             if target!= None and target != snail:
                 target.perma_buff(0,snail.ability_level)
def turkey_ability(turkey,target,prior_list=None):
     ## buying from 
     if turkey.base_hp >0:
    
        
        target.temp_buff(2*turkey.ability_level,3*turkey.ability_level)
def horse_ability(horse,target,prior_list=None):
     if horse.base_hp >0:
    
        print(horse.base_hp,"stater")
        target.temp_buff(0,horse.ability_level)
        
    #  print("Horse ability activated")
def otter_ability(otter,owner_board,prior_list=None):

    for unit in owner_board.board.random_n_amount_of_units(otter.ability_level,otter):

        unit.perma_buff(0,1) 
    
    ##when bought give random ally +1*lvl hp     
def mosquito_ability(mosqiuto,owner_board,prior_list=None):
        unit_board = owner_board.enemy_board.random_single_unit()
        owner_board.enemy_board.order[unit_board].take_damage(mosqiuto.ability_level,mosqiuto)   
        owner_board.enemy_board.order[unit_board].update_state("hurt")
        owner_board.enemy_board.order[unit_board].update(owner_board.enemy_board.order[unit_board].owner_board)
def ant_ability(self,owner_board,prior_list=None):
        buff_amount = self.ability_level
        owner_board.order[owner_board.random_single_unit()].temp_buff(buff_amount,buff_amount)      
def mouse_ability(mouse,owner_board,prior_list=None):
    

    if mouse.ability_level ==1:
       owner_board.item_store.add_item(Item("apple",0))
     
       #"Better Apple":[apple_1_ability],"Best Apple"
    elif mouse.ability_level == 2:
         owner_board.item_store.add_item(Item("Better Apple",0))
    else:
        owner_board.item_store.add_item(Item("Best Apple",0))
def duck_ability(duck,owner_board,prior_list=None):
    for unit in owner_board.shop_units:
        unit.perma_buff(0,duck.ability_level)
def beaver_ability(beaver,owner_board,prior_list=None):
   for unit in owner_board.board.random_n_amount_of_units(2,beaver):
        
        unit.perma_buff(beaver.ability_level,0) 
def cricket_ability(cricket,owner_board,prior_list):
   # the board given here doesn't work when we have the start of battle condiiton
    # print(cricket.owner_board)
    print(owner_board.order,len(owner_board.order),"cricker owner board")
    cricket.owner_board.order.insert(len(owner_board.order)+1,Unit("zombiecircket",cricket.ability_level,cricket.ability_level))# add it at the start of line in combat 
    cricket.owner_board.activate_summoners(cricket.owner_board.order[len(cricket.owner_board.order)-1])  
def fish_ability(fish,player_board,prior_list=None): 
      
       for unit in player_board.random_n_amount_of_units(2,fish):

        unit.perma_buff(fish.ability_level,fish.ability_level)  
def hedgehog_ability(hedgehog,board,prior_list):
    for unit in board.order+board.enemy_board.order:
        unit.take_damage(2*hedgehog.ability_level,hedgehog)
        print("hdege hog damaged")
def worm_ability(worm,owner_board,prior_list=None):
    

    if worm.ability_level ==1:
       owner_board.item_store.add_item(Item("apple",2))
    elif worm.ability_level == 2:
         owner_board.item_store.add_item(Item("Better Apple",2))
    else:
        owner_board.item_store.add_item(Item("Best Apple",2))
def giraffe_ability(giraffe,board,prior_list=None):
    pass # nearest key word will always happen to the nearest
def skippper(self= None,skipper = None,prior_list=None):
    return False
def rat_ability(rat,board,prior_list):
    for rat in range(rat.ability_level):
        board.enemy_board.order.insert(-1,Unit("dirty_rat",1,1))# add it at the start of line in combat 
        board.enemy_board.activate_summoners(board.enemy_board.order[-1])  
def pig_ability(pig,player_board,prior_list=None):
    player_board.gold = player_board.gold +pig.ability_level
def kangaroo_ability(kangaroo,owner_board,prior_list=None):
    kangaroo.temp_buff(kangaroo.ability_level,kangaroo.ability_level)
    kangaroo.ability_used = False
def peacock_ability(peacock,owner_board,prior_list=None):
    peacock.temp_buff(4*peacock.ability_level,0)
    peacock.ability_used = False
def flamingo_ability(flamingo,owner_board,prior_list = None):
    print(prior_list)
    #make it simple
    sliding_window = []
    for unit in prior_list:
      if unit == flamingo:
          exit
      sliding_window.append(unit)
      if len(sliding_window) >3:
          sliding_window.pop(0)
   
           
            
    for unit in sliding_window:
        
        unit.temp_buff(flamingo.ability_level,flamingo.ability_level)    
def sheep_ability(sheep,owner_board,prior_list = None):
    for _ in range(2):
        owner_board.order.insert(len(owner_board.order)+1,Unit("ram",sheep.ability_level*2,sheep.ability_level*2))# add it at the start of line in combat 
        sheep.owner_board.activate_summoners(sheep.owner_board.order[len(owner_board.order)+1])  
def dodo_ability(dodo,owner_board,prior_list = None):
    
    for index,unit in enumerate(owner_board.order):
        if unit == dodo:
            dodo_index = index
        if index == dodo_index+1:
            owner_board.order[index].temp_buff(0,dodo.Base_damage*(0.5*dodo.ability_level)) 
def camel_ability(camel,owner_board,prior_list=None):
    print("camel working")
    last_index = None
    # print(id(owner_board),"OWNER BOARD BY FUNCTRION")
    # print(id(camel.owner_board),"OWNER BORAD BY UNIT")
    for index,unit in enumerate(camel.owner_board.order):
  
        if unit == camel:
         owner_board.order[last_index].temp_buff(2*camel.ability_level,2*camel.ability_level) 
             
            #  print("buffed ",owner_board.order[last_index].Name)
        last_index= index
    print("onde")
       
    camel.ability_used = False
def giraffe_ability(giraffe,owner_board,prior_list):
    # give the nearest friend ahead (amount of the units depend on ability_level so)
    ### NOT BUFFING CHECK MEMORY ADDRESS
    giraffe_pos = None
    buff_list = []
    for index in owner_board.position_unit_dict:
        unit = owner_board.position_unit_dict[index]
        if unit == giraffe:
            giraffe_pos=index
        if unit != None and giraffe_pos != None and unit != giraffe:
            print(index,"INDEX ADDE")
            buff_list.append(index)
        

    for index in buff_list:
            print(index,"buffing this unit")
  

            owner_board.position_unit_dict[index].perma_buff(1,1)
def elephant_ability(elephant,owner_board,prior):    
    last_index = None
    for index,unit in enumerate(owner_board.order):
  
        if unit == elephant:
         for _ in range(elephant.ability_level):
            owner_board.order[last_index].take_damage(1,elephant)
             
            #  print("buffed ",owner_board.order[last_index].Name)
        last_index= index
    elephant.ability_used = False
def dolphin_ability(dolphin,owner_board,prior_list = None):
    ## add ability_level
    lowest_hp = 57
    lists_indexs =[]
    final_index = None
    for _ in range(dolphin.ability_level):
        for index,unit in  enumerate(owner_board.enemy_board.order):
            if unit.base_hp <= lowest_hp:
                if lowest_hp == unit.base_hp:
                    lists_indexs.append(index)
                else:
                    lowest_hp = unit.base_hp
                    lists_indexs = []
                    final_index = index
        
        if lists_indexs != []:
            
            final_index = np.random.choice(lists_indexs,1)[0]

        owner_board.enemy_board.order[final_index].take_damage(3,dolphin)
    # owner_board.order[dodo.place+1]
def dog_ability(dog,owner_board,prior_list=None):
    dog.temp_buff(2*dog.ability_level,1*dog.ability_level)
    dog.ability_used = False
def rabbit_ability(rabbit,target,prior_list=None):

    target.perma_buff(rabbit.ability_level,0)
def badger_ability(badger,owner_board,prior_list=None):
   
    print(len(prior_list))
    bigger_list = prior_list+owner_board.enemy_board.order
    for index in range(len(bigger_list)):
        print(index,"index count")
        
        
        if bigger_list[index] == badger:
            

            print("found badger")
            if index-0 >=0:
                bigger_list[index - 1].take_damage(badger.Base_damage,badger)
                print("damaged behind")
            if index +1 < len(bigger_list):
                
                bigger_list[index + 1].take_damage(badger.Base_damage,badger)
def ox_ability(ox,owner_board,prior_list=None):
    ox.buff_perk("melon")
    ox.temp_buff(1*ox.ability_level,0)
    ox.ability_used = False
def spider_ability(spider,owner_board,prior_list):
    owner_board.order.insert(-1,Unit(dict_of_pets[5][randint(9)],2*spider.ability_level,2*spider.ability_level))# add it at the start of line in combat 
    spider.owner_board.activate_summoners(spider.owner_board.order[-1]) 
def shunk_ability(shunk,owner_board,prior_list=None):
    highest_hp = -999
    lists_indexs =[]
    final_index = None
    for index,unit in  enumerate(owner_board.enemy_board.order):
        if unit.base_hp >= highest_hp:
            if highest_hp == unit.base_hp:
                lists_indexs.append(index)
            else:
                highest_hp = unit.base_hp
                lists_indexs = []
                final_index = index
        if lists_indexs != []:
            
            final_index = np.random.choice(lists_indexs,1)[0]
    owner_board.enemy_board.order[final_index].base_hp= int(owner_board.enemy_board.order[final_index].base_hp-(owner_board.enemy_board.order[final_index].base_hp*(0.33*shunk.ability_level)))
def hippo_ability(hippo,owner_board,prior_list=None):
    if hippo.alive:
        hippo.temp_buff(2*hippo.ability_level,2*hippo.ability_level)
        print("hippo ability worked")
        hippo.ability_used = False
    # if unit tier 4 double it 
def bison_ability(bison,owner_board,prior_list= None):
    for unit in owner_board.position_unit_dict.values():
        if unit != None:
            if unit.ability_level ==3:
                bison.perma_buff(1*bison.ability_level,2*bison.ability_level)
                break
def blowfish_ability(blowfish,owner_board,prior_list):

    index = owner_board.enemy_board.random_single_unit()
    owner_board.enemy_board.order[index].take_damage(blowfish.ability_level*3,blowfish) 
    blowfish.ability_used = False
def turtle_ability(turtle,owner_board,prior_list):
    ## add ability_level up
    last_index = None
    for index,unit in enumerate(owner_board.order):
        if unit == turtle:
            if last_index !=None:
                owner_board.order[last_index].buff_perk("melon")
        last_index = index
def squirrel_ability(squirrel,owner_board,prior_list):
    for item in range(len(owner_board.shop.item_shop.item_list)):
        owner_board.shop.item_shop.item_list[item].cost =  owner_board.shop.item_shop.item_list[item].cost - squirrel.ability_level
def penguin_ability (penguin,owner_board,prior_list):
     buff_units = []
     units_list = []
     
     for index in owner_board.position_unit_dict:
        if owner_board.position_unit_dict[index] !=  None:
             if owner_board.position_unit_dict[index].ability_level >1:
                 units_list.append(index)

     buff_units =np.random.choice(units_list,2)

     for index in buff_units:
        owner_board.position_unit_dict[index].perma_buff(penguin.ability_level,penguin.ability_level)  
def deer_ability(deer,owner_board,prior_list):
    for _ in range(deer.ability_level):
        owner_board.order.insert(len(owner_board.order)+1,Unit("bus",deer.ability_level*5,deer.ability_level*5))
        deer.owner_board.activate_summoners(len(owner_board.order)+1)  
        for unit in prior_list:
            print(unit.Name)
        owner_board.order[-1].buff_perk("chilli")
def whale_ability(whale,owner_board,prior_list):
    ## edit ability_level up 
    if not whale.isfull:
        
        for index,unit in enumerate(owner_board.order):
                
                if unit == whale:
                    if index+1 < len(owner_board.order):
                        whale.unit_in_mouth = copy.deepcopy(owner_board.order[index + 1])
                    
                        owner_board.order[index + 1].update_state("faint")
                        
                        owner_board.order[index + 1].update(owner_board)
                        owner_board.order[index + 1].alive = False
                        owner_board.order[index + 1].base_hp = -1
                        whale.isfull = True
                        owner_board.order[index].ablity_game_state = "faint"
                        print("FULLY EATEN")
                        
    
    else:               
        owner_board.order.insert(len(owner_board.order)+1,whale.unit_in_mouth)
        owner_board.activate_summoners(len(owner_board.order)+1)  
        whale.owner_board.order[len(owner_board.order)+1].update_state("summon-ed")
        whale.owner_board.order[len(owner_board.order)+1].update(whale.owner_board.order)
    whale.ability_used = False
def parrot_ability(parrot,owner_board,prior):
    parrot.ability_level = parrot.level
    for index,unit in enumerate(owner_board.position_unit_dict.values()):
        

        if unit == parrot:
            if index+1 < len(owner_board.position_unit_dict.values()):
                #   owner_board[index + 1] = owner_board[index + 1] 
                parrot.ablity_game_state = owner_board.position_unit_dict[index+1].ablity_game_state 
                parrot.ability = owner_board.position_unit_dict[index+1].ability
                print(parrot.ablity_game_state,"parrot ")
    parrot.ability_used = False
def armadillo_ability(armadillo,owner_board,prior_list):
    for index in range(len(owner_board.order+owner_board.enemy_board.order)):
    
        if index < len(owner_board.order):
        #    owner_board.order[index].base_hp  =  owner_board.order[index].base_hp+8 * armadillo.ability_level
           owner_board.order[index].temp_buff(0,8*armadillo.ability_level)
   
        else:
            index = len(owner_board.order) -index  -1
           
            # owner_board.enemy_board.order[index].base_hp  =  owner_board.enemy_board.order[index].base_hp+8 * armadillo.ability_level
            owner_board.enemy_board.order[index].temp_buff(0,8*armadillo.ability_level)
def rhino_ability(rhino,owner_board,prior_list):    
            
            rhino.ability_used = False 
            for index in range(len(owner_board.enemy_board.order)):
                index= index *-1 +1
                mult = 1
              
                if owner_board.enemy_board.order[index].base_hp <1 and not owner_board.enemy_board.order[index].alive:
                     continue
                    
                    # if  owner_board.enemy_board.order[index].alive:
                else:
                    if owner_board.enemy_board.order[index].tier == 1:
                        mult = 2 
                    owner_board.enemy_board.order[index].take_damage(rhino.ability_level*4*mult,rhino)
                    
                    break
def monkey_ability(monkey,owner_board,prior_list):
    last_unit = None
  
    for index in [4,3,2,1,0]:
      
        if owner_board.position_unit_dict[index] != None:
         last_unit = index
        
         break
    owner_board.position_unit_dict[last_unit].perma_buff(2*monkey.ability_level,3*monkey.ability_level)
def scorpion_ability(scorpion,owner_board,prior):
  
    # if target == scorpion:
     
    scorpion.buff_perk("peanut")
def crocodile_ability(crocodile,owner_board,prior):
    for _ in range(crocodile.ability_level):
        owner_board.enemy_board.order[0].take_damage(8,crocodile)
def cow_ability(cow,owner_board,prior):
    dict_of_cow_level = {1:[Item("milk",0),Item("milk",0)],2:[Item("better milk",0),Item("better milk",0)],3:[Item("best milk",0),Item("best milk",0)]}
    owner_board.item_shop.item_list = dict_of_cow_level[cow.ability_level]
def seal_ability(seal,target):
    random_list =[]
    if target == seal:
        for index in seal.owner_board.position_unit_dict:
            if seal.owner_board.position_unit_dict[index] != None:
                random_list.append(index)

        
        for unit in np.random.choice(random_list,3):
            # print(seal.owner_board.position_unit_dict.keys(),"seal keys")
            seal.owner_board.position_unit_dict[unit].perma_buff(seal.ability_level,0)
def chicken_ability(chicken,owner_board,prior):
    for _ in range(chicken.level):
        chicken.owner_board.order.insert(len(owner_board.order)+1,Unit("chick",1,chicken.Base_damage//2))# add it at the start of line in combat 
        chicken.owner_board.activate_summoners(len(owner_board.order))  
def shark_ability(shark,owner_board,num_of_faints):
    shark.temp_buff(1*shark.ability_level*num_of_faints,2*shark.ability_level*num_of_faints)
   
# defpr
dict_of_pets= {1:["duck","beaver","otter","pig","ant","mosqutio","mouse","fish","cricket","horse"],
               3:["snail","crab","swan","rat","hedgehog","peacock","flmingo","worm","kangaroo","spider"],
               5:["dodo","badger","dolphin","giraffe","elephant","camel","rabbit","ox","dog","sheep"]
               ,7:["shunk","hipoo","pufferfish","turtle","squrial","penguin","deer","whale","parrot"],
               9:["scropion","crocidle","rhino","monkey","armadilo","cow","seal","chicken","shark","turkey"]
               ,11:["leopard","boar","tiger","wolvrine","gorilla","dragon","mamotth","cat","snake","fly"]}
status = ["buy","sell","faint","none","start_of_battle","start_of_turn","friend_ahead_attacks"]

dict_of_tiers = {"duck":1,"beaver":1,"otter":1,"pig":1,"ant":1,"mosqutio":1,"mouse":1,"fish":1,"cricket":1,"horse":1,"bus":1,"chick":1,
                "snail":2,"crab":2,"swan":2,"rat":2,"hedgehog":2,"peacock":2,"flmingo":2,"worm":2,"kangaroo":2,"spider":2,
                "dodo":3,"badger":3,"dolphin":3,"giraffe":3,"elephant":3,"camel":3,"rabbit":3,"ox":3,"dog":3,"sheep":3,
                "shunk":4,"hippo":4,"pufferfish":4,"turtle":4,"squrial":4,"penguin":4,"deer":4,"whale":4,"parrot":4,
                "scorpion":5,"crocodile":5,"rhino":5,"monkey":5,"armadilo":5,"cow":5,"seal":5,"chicken":5,"shark":5,"turkey":5,
                "leopard":6,"boar":6,"tiger":6,"wolvrine":6,"gorilla":6,"dragon":6,"mamotth":6,"cat":6,"snake":6,"fly":6}


ability_dict ={"ant":[ant_ability,"faint"],"otter":[otter_ability,"buy"],"mosqutio":[mosquito_ability,"start_of_battle"],
               "duck":[duck_ability,"sell"],"beaver":[beaver_ability,"sell"],"pig":[pig_ability,"sell"],"mouse":[mouse_ability,"sell"],
               "fish":[fish_ability,"level_up"],"cricket":[cricket_ability,"faint"],"horse":[horse_ability,"summon"],"zombiecircket":[skippper,None],
               "bee":[skippper,None], "turkey" :[turkey_ability,"summon"],"crab":[crab_ability,"start_of_battle"],"swan":[swan_ability,"start_of_turn"],
               "snail":[snail_ability,"start_of_turn"],"worm":[worm_ability,"start_of_turn"],"hedgehog":[hedgehog_ability,"faint"],
               "rat":[rat_ability,"faint"],"dirty_rat":[skippper,None],"kangaroo":[kangaroo_ability,"friend_ahead_attacks"],
               "peacock":[peacock_ability,"hurt"],"flamingo":[flamingo_ability,"faint"],"ram":[skippper,None],"sheep":[sheep_ability,"faint"],
               "dodo":[dodo_ability,"start_of_battle"],"dolphin":[dolphin_ability,"start_of_battle"],"giraffe":[giraffe_ability,"end_of_turn"],
               "camel":[camel_ability,"hurt"],"elephant":[elephant_ability,"after_attack"],"dog":[dog_ability,"summon"],"badger":[badger_ability,"faint"],
               "rabbit":[rabbit_ability,"eat food"],"ox":[ox_ability,"faint_ahead"],"spider":[spider_ability,"faint"],"shunk":[shunk_ability,"start_of_battle"],
               "hippo":[hippo_ability,"knock_out"],"bison":[bison_ability,"end_of_turn"],"blowfish":[blowfish_ability,"hurt"],"turtle":[turtle_ability,"faint"],
               "squirrel":[squirrel_ability,"start_of_turn"],"penguin":[penguin_ability,"end_of_turn"],"bus":[skippper,None],"deer":[deer_ability,"faint"],
               "whale":[whale_ability,"start_of_battle"],"parrot":[parrot_ability,"end_of_turn"],"armadillo":[armadillo_ability,"start_of_battle"],
               "rhino":[rhino_ability,"knock_out"],"monkey":[monkey_ability,"end_of_turn"],"scorpion":[scorpion_ability,"summon-ed"],"crocodile":[crocodile_ability,"start_of_battle"],
               "cow":[cow_ability,"buy"],"seal":[seal_ability,"eat food"],"chicken":[chicken_ability,"faint"],"chick":[skippper,None],"shark":[shark_ability,"ally_fainted"]} 
  
modifier_dict= {"meat":[0,3],None:[0,0],"melon":[20,0],"chilli":[0,0],"peanut":[0,0]}
class Unit: 
    ## add cap to 50 hp and 50 damage
    def __init__(self,Name,Damage,Hp):
        self.Name = Name
        self.base_hp = Hp
        self.perma_buff_bucket= [0,0]
        self.Base_damage = Damage
        # x.ability_flag and not x.activated_flag
        self.Cost =3 
        self.level=1
        self.tier=dict_of_tiers[Name] #bus and chickens are tier 1 by default
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
        self.perk_used = False
        self.position = None
        self.round_perk = None
        self.perk_disable = False
        self.isfull=False
        self.unit_in_mouth = False
        self.ability_level = self.level
        
    def update_state(self,state):
        self.state = state
    def increase_level(self,level):
        self.level  = level## WIP
    def update(self,owner_board,optional_board = None):
        # update only makes the ability in que be ware of this
        #another object has to force the ability to activate 
     
        self.owner_board = owner_board
        # print(self.state)
       
        # print(self.ablity_game_state,self.state)
        if (self.state==self.ablity_game_state) and not self.ability_used:
            self.ability_used = True
        
            self.ability(self,self.owner_board,optional_board) ## We must send the board to avoid any issues later on 
            
        
        if self.perk !=None:
         
         
         if ( self.state == self.perk_activation ) and not self.perk_used:
             
             self.perk_ability(self,optional_board)
             self.perk_used = True         
         if self.perk_disable:
            if (self.state == self.perk_disable):
              
                self.perk = None
    def attack(self,enemy):
        
        enemy_modifier=[0,0]
        modifier =[0,0]
        temp_modifier= [0,0]

        
        for unit in [self,enemy]:
                temp_modifier= [0,0]
                perk_list = modifier_dict[unit.perk]
       
                temp_modifier = [temp_modifier[0]+perk_list[0],temp_modifier[1]+perk_list[1]]

                if unit == self:
                    modifier=copy.deepcopy(temp_modifier)

                else:
                    enemy_modifier=copy.deepcopy(temp_modifier)
        
        # enemy.base_hp = (enemy.base_hp+enemy_modifier[0]) - (self.Base_damage+modifier[1])
        
        enemy_damage  = (enemy_modifier[0] - (self.Base_damage+modifier[1]))*-1
        
        if  enemy_damage<0:
            enemy_damage = 0
        
        enemy.base_hp =  enemy.base_hp - enemy_damage
        
        if len(enemy.owner_board.order)>1 and self.perk=="chilli":
            perk_list = modifier_dict[enemy.owner_board.order[-2].perk]
            temp_modifier = [perk_list[0],temp_modifier[1]+perk_list[1]]
            chilli_damage  = (perk_list[0] - (5))*-1
        
            if  chilli_damage<0:
                 chilli_damage = 0
            enemy.owner_board.order[-2].base_hp = enemy.owner_board.order[-2].base_hp - chilli_damage
            enemy.owner_board.order[-2].update_state("hurt")
            enemy.owner_board.order[-2].update(enemy.owner_board.order[-2].owner_board)
            
            if enemy.owner_board.order[-2].base_hp  <= 0:
                enemy.owner_board.order[-2].alive = False
                enemy.owner_board.order[-2].base_hp = -1
        self_damage = (modifier[0] - (enemy.Base_damage+enemy_modifier[1]))*-1
                        
        if  self_damage<0:
            self_damage = 0
    
        self.base_hp = self.base_hp - self_damage

        
        ## remeber the two units attack at the same moment so don't apply the damage before 
        # if self.perk On_damage:
        # reduce damage
        # if self.perk On_damage:
        # reduce damage

        if len(self.owner_board.order)>1 and enemy.perk=="chilli":
            perk_list = modifier_dict[self.owner_board.order[-2].perk]
            temp_modifier = [perk_list[0],temp_modifier[1]+perk_list[1]]
            chilli_damage  = (perk_list[0] - (5))*-1

            if  chilli_damage<0:
                 chilli_damage = 0
            self.owner_board.order[-2].base_hp = self.owner_board.order[-2].base_hp - chilli_damage
          
            if self.owner_board.order[-2].base_hp  <= 0:
                self.owner_board.order[-2].alive = False
                self.owner_board.order[-2].base_hp = -1
            else:
                self.owner_board.order[-2].update_state("hurt")
                self.owner_board.order[-2].update(self.owner_board.order[-2].owner_board)

          
        print("one shot", self.perk =="peanut")  
        if (self.perk == "peanut"  and self_damage> 20) or (self.perk == "peanut" and enemy.perk != "melon"):  
            enemy.base_hp = 0
            
        if (enemy.perk == "peanut"  and enemy_damage> 20) or (enemy.perk == "peanut" and self.perk != "melon"):  
            self.base_hp = 0
        ## check if they have less hp than started?
            
        
       
        print(self.Name, " attacked ",enemy.Name )
        print(enemy.Name, " attacked ",self.Name )
        
        
        if enemy.base_hp  <= 0:
            
            enemy.alive = False
            enemy.base_hp = -1
                  
        else:
            enemy.update_state("hurt")
            enemy.update(enemy.owner_board)
            enemy.update_state("after_attack")
            enemy.update(enemy.owner_board)

        if self.base_hp <= 0:
            self.alive = False
            self.base_hp = -1 
            
        else:
            self.update_state("hurt")
            self.update(self.owner_board)
            self.update_state("after_attack")
            self.update(self.owner_board)        

        if self.alive and not enemy.alive:
            self.update_state("knock_out")
            self.update(self.owner_board)  
        elif not self.alive and enemy.alive:
            enemy.update_state("knock_out")
            enemy.update(enemy.owner_board)
            
    def buff_perk(self,perk):
        Item(perk).give_perk(self)


        
    def alive_check(self):
        return self.alive
    def perma_buff(self,Damage,Hp):
        # print("perma_buffing")
        self.base_hp = self.base_hp+Hp
        self.Base_damage=self.Base_damage + Damage
        self.perma_buff_bucket[0] =  self.perma_buff_bucket[0]+Hp
        self.perma_buff_bucket[1] =  self.perma_buff_bucket[1]+Damage
    def temp_buff(self,Damage,Hp):
        # print(Hp,Damage,"temp buff")
        self.base_hp = self.base_hp+Hp
        self.Base_damage=self.Base_damage + Damage
        self.temp_buff_hp = self.temp_buff_hp+ Hp
        self.temp_buff_damage=self.temp_buff_damage +Damage
    
    def round_end(self):
        self.alive = True
        self.activated_flag = False
        self.base_hp=self.base_hp - self.temp_buff_hp
        self.Base_damage=self.Base_damage-self.temp_buff_damage
        self.temp_buff_damage = 0
        self.temp_buff_hp = 0

    def take_damage(self,damage_amount,attacker):
        self.base_hp= self.base_hp -damage_amount
        # if self.perk On_damage:
        # reduce damage

        if damage_amount > 0:
            self.update_state("hurt")
            self.update(self.owner_board)
        if self.base_hp <= 0:
            print(id(attacker),"rhino ID")
            self.alive = False
            attacker.update_state("knock_out")
            attacker.update(attacker.owner_board)
     
            
class Board:
    # start board with a draw so snail doesn't give hp
    def __init__(self):
        self.order = []
        self.start_order = []
        self.board_state= None
        self.alive = True
        self.enemy_board = None
        self.shop = None
        self.targetable_units =[]
        self.position_unit_dict = {0:None,1:None,2:None,3:None,4:None}
        self.last_round_lost = False
        self.fainted_this_round = 0
    def swap_unit_place(self,origin,end):
             if origin >5 or end>5:
                 print("Out of range")
             if self.position_unit_dict[origin] == None:
                 print("Failure to move due to moving an empty slot")
             
             if self.position_unit_dict[end].Name != self.position_unit_dict[origin].Name:
                 print("Units is already in the space")

                ##DRY TRY TO MAKE A FUNCTION 
             if  self.position_unit_dict[end].Name == self.position_unit_dict[origin].Name and not self.position_unit_dict[origin].level == 3:
                print("LEVELING UP ")
                self.position_unit_dict[end].level_amount = self.position_unit_dict[end].level_amount  +self.position_unit_dict[origin].level_amount +1
                self.position_unit_dict[end].perma_buff(self.position_unit_dict[origin].level_amount +1,self.position_unit_dict[origin].level_amount + 1) 

                if self.position_unit_dict[end].level == 1 and self.position_unit_dict[end].level_amount ==2 :
                    print("LEVEL 2 ")
                    self.position_unit_dict[end].update_state("level_up")
                    self.position_unit_dict[end].update(self)
                    self.position_unit_dict[end].level = self.position_unit_dict[end].level+1
                    self.position_unit_dict[end].level_amount =self.position_unit_dict[end].level_amount - 2

                if self.position_unit_dict[end].level == 2 and self.position_unit_dict[end].level_amount >2:
                    self.position_unit_dict[end].update_state("level_up")
                    self.position_unit_dict[end].update()
                    self.position_unit_dict[end].level_amount =self.position_unit_dict[end].level_amount - 3
                    self.position_unit_dict[end].level = self.position_unit_dict[end].level+1
             self.position_unit_dict[origin] = None

    
            
    def show_order(self):
        for position in [0,1,2,3,4]:
            units = self.position_unit_dict[position]
            if units != None:
               print(position,units.Name, units.base_hp, units.Base_damage)
        # print(self.order,"show order")
        
    def amount_units(self):
        return len(self.order)
    def remove_fainted_list(self):
      
        # order_copy = copy.deepcopy(self.order)s
        fainted_this_round =0
        unit_fainted= False
        for index,unit in enumerate(self.order):
        
            if not unit.alive:
                unit.update_state("faint")
                unit.update(self,self.order)
                fainted_this_round = fainted_this_round +1
                unit_fainted = True
                if index-1 >= 0:
                    self.order[index-1].update_state("faint_ahead")
                    self.order[index-1].update(self,self.order)
        self.order = [x for x in self.order if  x.alive_check()]
        if unit_fainted:
            for unit in self.order:
                unit.update_state("ally_fainted")
                unit.update(self,fainted_this_round)
        
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
       
        for position,units in enumerate(self.order):
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
        for position,units in enumerate(other_board.order[::-1]):
            
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
    
    def random_n_amount_of_units(self,num_ally,exempt = None):
        self.create_targetable_list(exempt)
        # print(num_ally,len(self.targetable_units),"num ally and len targetable")
        length_of_targetable_list  = len(self.targetable_units)
        if length_of_targetable_list !=0:
       
          if length_of_targetable_list <= num_ally:
              return self.targetable_units
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
    def activaite_food_eaters(self,target):
        for unit in self.position_unit_dict.values():
            if unit != None:
                if unit.ablity_game_state == "eat food":
                    print(unit.state,unit.Name,"Unit staeeeeeeee")
                    unit.ability(unit,target)
    def activate_summoners(self,target):
        if self.order!=[]:
         for unit in self.order:
            if unit != None:
                if unit.ablity_game_state == "summon":
                    # print(unit.state,unit.Name,"Unit staeeeeeeee")
                    unit.ability(unit,target)
        else:
         for unit in self.position_unit_dict.values():
            if unit != None:
                if unit.ablity_game_state == "summon":
                    # print(unit.state,unit.Name,"Unit staeeeeeeee")
                    unit.ability(unit,target)
    def start_of_battle_for_units(self):
        for unit in self.order:
            unit.update_state("start_of_battle")
            unit.update(self)
    def add_unit_attack_q(self,unit):
        pass
    def shop_linking(self,shop):    
        self.shop = shop
    def reset_board(self,board2):
        ##needs more testing
        for units in self.start_order+board2.start_order:
            units.round_end()
        self.order = self.start_order
        board2.order = board2.start_order
        self.order=[]
        board2.order = [    ]
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
    def create_targetable_list(self,exempt=None):
        self.targetable_units =[]
        for unit in self.position_unit_dict.values(): 
          
            
            if unit != None:
                if unit != exempt:
                    self.targetable_units.append(unit)
    def start_of_turn_for_units(self):
        self.create_targetable_list()
        for unit in self.targetable_units: 
            unit.update_state("start_of_turn")
            unit.update(self)
    def end_of_turn_for_units(self):
        for index in self.position_unit_dict:
            unit = self.position_unit_dict[index]
            if unit != None:
                unit.update_state("end_of_turn")
                unit.update(self)
    def create_board_for_battle(self):
        # process list   
        list_for_battle = self.position_unit_dict.values()
        # print(list_for_battle,"list for battle")
        temp_ = []
        for elemnt in list_for_battle:
                if elemnt != None:
                    
                    temp_.append(elemnt)         

        
        self.order = copy.deepcopy(temp_)
def battle_phase(board1,board2,round_num = 320,visible = False):

    battle_finished = False
    round_count= 0
   
    if visible:
        board1.show_order_display(board2)
    board1.enemy_board_linking(board2)
    board1.create_board_for_battle()
    board2.create_board_for_battle()
    # print(board1.total_of_hp_and_damage(),"total hp limit")
    # print("board 2")
    # board2.show_order_display()
    # battle_phase(board1,board2)
   
    while not battle_finished:
            ##pre battle stuff WIP
            ###
            
                
            round_count= 1+round_count
            #mid attacl
            if visible:
                print("======================")
                print("┃                    ┃")
                print("┃      round  ",round_count,"    ┃")
                print("┃                    ┃")
                print("======================")
            
            if round_count ==1:
              
                # board1.show_order_display(board2)
                if visible:
                 board1.show_order_display(board2)
                board1.start_of_battle_for_units()
                board2.start_of_battle_for_units()
                print("START THE ROUND")
             
                board1.remove_fainted_list()
                board2.remove_fainted_list()

                if round_num == "start":
                    board1.show_order_display(board2)
                    return board1.total_of_hp_and_damage()                   
              

            else:
                board1.mid_battle_state(board2)
            board2.order[-1].attack(board1.order[-1])
            
            if board2.order[0] != board2.order[-1]:
            
                board2.order[-2].update_state("friend_ahead_attacks")
               
                board2.order[-2].update(board2)

            if board1.order[0] != board1.order[-1]:
                
                 board1.order[-2].update_state("friend_ahead_attacks")
                
                 board1.order[-2].update(board1)
            
            board1.remove_fainted_list()
            board2.remove_fainted_list()

            board1.update_board()
            board2.update_board()
            
            board1.remove_fainted_list()
            board2.remove_fainted_list()
            board1.update_board()
            board2.update_board()
            # board1.update()
            
            #post attack
            
            # board1.update_board()
            # board2.update_board()
            # results
            # print(board1.amount_units())
            # print(board2.amount_units())
        
            if round_count == round_num:
                board1.show_order_display(board2)
                return board1.total_of_hp_and_damage()      

            if board1.amount_units() == 0 and  board2.amount_units()!=0:
                    print("board 2 wins")
                    battle_finished = True
                    if visible:
                        board1.show_order_display(board2)
                    # return ("Lost")
            elif board1.amount_units() != 0 and board2.amount_units()==0:
                    print("board 1 wins")
                    battle_finished = True
                    if visible:
                        board1.show_order_display(board2)
                    # return ("Win")
                
            elif board1.amount_units() == 0 and board2.amount_units()==0:
                    print("draw")
                    battle_finished = True
                    return None
                    # return "draw"
            else:
                    if visible:
                      board1.show_order_display(board2)
                
                    continue
            
            
    ##

  
dict_of_pets= {1:["duck","beaver","otter","pig","ant","mosqutio","mouse","fish","cricket","horse"],
               3:["snail","crab","swan","rat","hedgehog","peacock","flmingo","worm","kangaroo","spider"],
               5:["dodo","badger","dolphin","giraffe","elephant","camel","rabbit","ox","dog","sheep"]
               ,7:["skunk","hipoo","pufferfish","turtle","squrial","penguin","deer","whale","parrot"],
               9:["scropion","crocidle","rhino","monkey","armadilo","cow","seal","chicken","shark","turkey"]
               ,11:["leopard","boar","tiger","wolvrine","gorilla","dragon","mamotth","cat","snake","fly"]}

dict_of_pets_with_stats ={"duck":Unit("duck",2,3),"beaver":Unit("beaver",3,2),"otter":Unit("otter",1,3),"pig":Unit("pig",4,1),"ant":Unit("ant",2,2),"mosqutio":Unit("mosqutio",2,2),
                          "mouse":Unit("mouse",1,2),"fish":Unit("fish",2,3),"cricket":Unit("cricket",1,2),"horse":Unit("horse",2,1),"turkey":Unit("turkey",3,4),"swan":Unit("swan",2,1),
                          "crab":Unit("crab",4,1),"worm":Unit("worm",1,2),"hedgehog":Unit("hedgehog",4,2),"rat":Unit("rat",3,6),"peacock":Unit("peacock",2,5),"sheep":Unit("sheep",2,2),
                          "dodo":Unit("dodo",4,2),"dolphin":Unit("dolphin",4,3),"camel":Unit("camel",2,4),"elephant":Unit("elephant",3,7),"spider":Unit("spider",2,2),"ox":Unit("ox",1,3),
                          "shunk":Unit("shunk",3,5),"hippo":Unit("hippo",4,7)}

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
                
                # summon-ed
                
                #bought effects
                # self.shop_units[index].bought = True
                self.shop_units[index].update_state("buy")
                self.shop_units[index].owner_board = self.board
                self.shop_units[index].update(self)
                # self.shop_units[index].update_state("summoned")
                
                self.board.activate_summoners(self.shop_units[index])               
                self.board.position_unit_dict[place]= self.shop_units[index]

                self.board.position_unit_dict[place].update_state("summon-ed")
                self.board.position_unit_dict[place].update(self.board)
                self.board.position_unit_dict[place].position =  place

                # np.insert( self.player_units,place,self.shop_units[index]) 
                # print(self.shop_units[index],"shop unit index")

                self.shop_units= np.delete(self.shop_units,index) 
    
                # print("bought the ",self.shop_units[0].Name,place,"bought test")

                ##DRY TRY TO MAKE A FUNCTION 
        elif  self.board.position_unit_dict[place].Name == self.shop_units[index].Name and not self.shop_units[index].level == 3:
             print("LEVELING UP ")
             self.board.position_unit_dict[place].level_amount = self.board.position_unit_dict[place].level_amount  +self.shop_units[index].level_amount +1
             self.board.position_unit_dict[place].perma_buff(self.shop_units[index].level,self.shop_units[index].level)
             self.shop_units= np.delete(self.shop_units,index) 
             if self.board.position_unit_dict[place].level == 1 and self.board.position_unit_dict[place].level_amount ==2 :
                 print("LEVEL 2 ")
                 self.board.position_unit_dict[place].update_state("level_up")
                 self.board.position_unit_dict[place].update(self.board)
                 self.board.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1
                 self.ability_level = self.ability_level +1 
                 self.board.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 2

             if self.board.position_unit_dict[place].level == 2 and self.board.position_unit_dict[place].level_amount >2:
                 self.board.position_unit_dict[place].update_state("level_up")
                 self.board.position_unit_dict[place].update(self.board)
                 self.board.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 3
                 self.board.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1
                 self.ability_level = self.ability_level +1 
                 #####WIP ADD BUY UNITS USE THEIR UPGRADED ABILITY 
        else:
             print("UNIT IS ALREADY IN THAT PLACE")
        
    def link_item_shop(self,item_shop):
        self.item_shop = item_shop
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
            # if self.board.position_unit_dict[index].Name == "pig": ## just use the normal function
            #     self.gold= self.gold + self.board.position_unit_dict[index].level
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

    def gold_override(self,num):
            #dev tool to enable testing
            self.gold = num
def apple_ability(target):
      
        target.perma_buff(1,1)

   
def apple_1_ability(target):
    target.perma_buff(2,2)
def apple_2_ability(target):
    target.perma_buff(3,3)
def honey_ability(target,optional_board):
        ## Needs testing
       
        optional_board.insert(0,Unit("bee",1,1))# add it at the start of line in combat 
        target.owner_board.activate_summoners(target.owner_board.order[0])  
        target.perk_used =True
def cupcake_ability(target):
    target.temp_buff(3,3)

def  milk_ability(target):
        target.perma_buff(1,2)
   
def milk_1_ability(target):
    target.perma_buff(2,4)
def milk_2_ability(target):
    target.perma_buff(3,6)

dict_of_items_ability = {"apple":[apple_ability,"ability","buff"],"better apple":[apple_1_ability,"ability","buff"],
                         "best apple":[apple_2_ability,"ability","buff"],"honey":[honey_ability,"perk","buff"],
                         "meat":[None,"perk","buff"],"cupcake":[cupcake_ability,"ability","buff"],"melon":[None,"perk","buff","hurt"]
                         ,"chilli":[None,"perk","buff"],"peanut":[None,"perk","buff"],"milk":[milk_ability,"ability","buff"],
                         "better milk":[milk_1_ability,"ability","buff"],"best milk":[milk_2_ability,"ability","buff"]}
class Item: # becareful there are many types of abiltiies from buffs to reducing damage once 
    ## link to the player unit board
    def __init__(self,name,cost = 3):
        self.name = name
        self.ability = dict_of_items_ability[name][0]
        print(dict_of_items_ability[self.name][1],"self name 1",self.name)
        self.cost = cost
    def change_cost(self,new_cost):
        self.cost = new_cost

    def use_ability(self,target):
        # print(dict_of_items_ability[self.name][1],"self name 133")
           
        if dict_of_items_ability[self.name][1]  == "ability":
            
            self.ability(target)
        else:

            
            self.give_perk(target)

   
    def give_perk(self,target):
         ## Carry over perks otherwise bugs will happen
        self.owner = target
        target.perk = self.name # removing to save some space form the str
        target.perk_activation = dict_of_items_ability[self.name][1]
        target.perk_ability = self.ability = dict_of_items_ability[self.name][0]
        target.perk_type = dict_of_items_ability[self.name][1]
        if len(dict_of_items_ability[self.name])>3:
            target.perk_disable = dict_of_items_ability[self.name][3]
        
        print("given_perk")

dict_of_items_with_stats = {"apple": Item("apple"), "better Apple":Item("better apple"),"best apple":("best apple"),"honey":Item("honey")
                            ,"meat":Item("meat") ,"cupcake":Item("cupcake"),"melon":Item("melon"),"milk":Item("milk"),"better milk":Item("better milk"),"best milk":("best milk") }

dict_of_items={1:["apple","honey"],3:["pill","meat","cupcake"],5:["salad","onion"],7:["canned food","pear"],9:["pepper","choco","sushi"],11:["steak","melon","mushroom","pizza"]}
class Item_shop:
    ## add freezing, refreshing, generating 
    def __init__(self,unit_store):
        self.linked_shop = unit_store
        
        self.turn = unit_store.turn # might cause issues 
        self.item_pool = np.array([])
        self.item_list=list()
        self.amount_of_items = 1 
        self.add_item_pool()
        self.temp_shop = []
        self.generate_items()
    def increase_turn(self):
        self.turn=self.turn+1
        if self.turn ==5 or self.turn == 9:
            self.amount_of_items = self.amount_of_items+1
        if self.turn in [3,7,9,11]:
            self.add_item_pool()
    def add_item_pool(self):
        self.item_pool=  np.concatenate((self.item_pool,dict_of_items[self.turn]))
    def buy(self,index,target):
   
        if index < len(self.item_list):
            
            if self.item_list[index] != None :
            
              if self.item_list[index].cost <=  self.linked_shop.gold:
                  self.linked_shop.board.activaite_food_eaters(self.linked_shop.board.position_unit_dict[target])
                  self.item_list[index].use_ability(self.linked_shop.board.position_unit_dict[target])
              else:
                  print("Not enough gold")
            else:
                print("no unit in place")
        else:
            print("out of range")
            
            # activate the item
    def generate_items(self):
        self.item_list = np.random.choice(self.item_pool,size=self.amount_of_items,replace=False)
        for item in self.item_list:                      
            new_item = dict_of_items_with_stats[item]
            # self.shop_units = np.insert(self.player_units,index,new_unit)
            self.temp_shop.append(new_item)
            # self.shop_units= np.delete(self.shop_units,index)
            # np.delete(self.shop_units,index)
            # self.player_units = np.insert(self.player_units,index,new_unit)
        self.item_list = copy.deepcopy(self.temp_shop)
        self.temp_shop=[]#empty to avoid memory issues 
    def reroll(self):
        ## only called from it's parent shop (hopefully)
        if self.gold >0:

            self.generate_items()
            
        else:
            print(self.gold)
    def add_item(self,item):
        #dev tool to enable testing
        self.item_list.append(item)
    def show_items(self):
        print("Showing items")
        print(self.item_list)
        for item in self.item_list:
            print(item.name,item.cost)
    def edit_shop(self,shop):
        self.temp_shop = []
        self.shop_units =  shop
        for item in shop:
            # damage,hp  = dict_of_pets_with_stats[unit]
            
          
            
             
            self.temp_shop.append(dict_of_items_with_stats[item])
           
            # self.shop_units= np.delete(self.shop_units,index)
            # np.delete(self.shop_units,index)
            # self.player_units = np.insert(self.player_units,index,new_unit)
        self.item_list = copy.deepcopy(self.temp_shop)
        print(self.shop_units,"edit _ shop ")
# def honey_ability(honey,board):


class Player:
    def __init__(self,board,unit_store,item_shop):
        self.round_counter =0
        self.player_hp = 6
        self.board = board
        self.unit_store = unit_store
        self.item_shop = item_shop

class Match:
    def __init__(self):
        self.round_counter = 0
    def increase_round(self):
        self.round_counter = self.round_counter +1
    def player_v_player(self,p1,p2):
        

        p1.start_of_turn_for_units()
        p2.start_of_turn_for_units()

        p1.end_of_turn_for_units()
        p2.end_of_turn_for_units()
        battle_results = battle_phase(p1,p2)
        if battle_results == True:
            p2.player_hp = p2.player_hp -1 
            p2.last_round_lost = True
            p1.last_round_lost = False
        elif battle_results == False:
            p1.player_hp = p1.player_hp -1 
            p1.last_round_lost = True
            p2.last_round_lost = False

    def full_match(self,p1,p2):
        if p1.player_hp !=0 and p2.player_hp !=0:

            
            self.player_v_player(p1,p2)
    def buy_window(self):
        pass
        ## Allow it to be a time frame for the AI to buy
        
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

# board = Board()
# shop= Unit_store()
# board.shop_linking(shop)
# shop.link_to_board(board)
# shop.generate_units()
# # shop.reroll()

# shop.edit_shop([["horse",1,1],["pig",1,1],["pig",1,1],["pig",1,1]]) ## another is buffed
# shop.buy(0,4)   
# shop.buy(1,2)
# shop.buy(1,3)
# shop.buy(0,1)   

# board = Board()
# shop= Unit_store()
# item_shop= Item_shop(shop)
# board.shop_linking(shop)
# shop.link_to_board(board)

# shop.gold_override(9999)

# shop.edit_shop([["horse",1,1],["pig",2,2]])
  
# shop.buy(0,1)
# shop.buy(0,4)
# item_shop.show_items()
# item_shop.edit_shop(["honey"])
# item_shop.buy(0,1)

# total_hp =battle_phase(board,board,1,6)

# print(total_hp,"total") 



# shop.buy(1,4)
# Bee getting buffed by the horse even if the horse dies 




# item_shop.buy(1,3)



# board.show_order_display(board)
# total_hp =battle_phase(board,board, 1,6)
# print(board.position_unit_dict[4].base_hp)
# print(total_hp,"total") 


# total_hp = board.total_of_hp_and_damage_prebattle()


# honey
# board = Board()
# shop= Unit_store()
# board.shop_linking(shop)
# shop.link_to_board(board)
            
# shop.edit_shop([["cricket",1,1],["beaver",1,1],["beaver",1,1]])
        
# shop.buy(0,4)

# total_hp =battle_phase(board,board, 1)


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
###
  
board = Board()
shop= Unit_store()
item_shop= Item_shop(shop)
board.shop_linking(shop)
shop.link_to_board(board)   
shop.link_item_shop(item_shop)
shop.generate_units()
shop.gold_override(9999)
board.last_round_lost = True    
                        # shop.reroll()
shop.edit_shop([["pig",1,1],["pig",1,1],["shark",1,1]])
shop.buy(0,4)  
shop.buy(0,1)
shop.buy(0,3)   
board.start_of_turn_for_units()
board.end_of_turn_for_units()
item_shop.show_items()
board_2 = copy.deepcopy(board)

# board_2.position_unit_dict[4] = Unit("pig",1,19)
# board_2.position_unit_dict[4].buff_perk("peanut")
total_hp =battle_phase(board,board_2, 1,"visable")
    

###


# board.start_of_turn_for_units()
# board.end_of_turn_for_units()
#         # board.shop.gold_check()#



class CustomTests(unittest.TestCase):
    def test_otter_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
    
        shop.edit_shop([["otter",1,1],["otter",1,1],["otter",1,1]])
 
        shop.buy(0,4)
        shop.buy(1,2)
        shop.buy(0,1)    
    
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
    def test_leveling_up_unit_without_ability(self):
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
        self.assertEqual([board.position_unit_dict[4].level,board.position_unit_dict[4].level_amount],[2,0],"leveling test without ability failed")
    def test_fish_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        ### TODO perma buffs aren't removed when adding units 
        shop.gold_override(9999)
        shop.edit_shop([["fish",2,2],["fish",1,1],["fish",1,1],["duck",1,1]]) ## another is buffed
        shop.buy(0,4)   
        shop.buy(1,4)
        shop.buy(1,3)
        shop.buy(0,4)   

        self.assertEqual([board.position_unit_dict[3].base_hp,board.position_unit_dict[3].Base_damage],[2,2],"fish ability failed")
    def test_horse_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        ### TODO perma buffs aren't removed when adding units 
        shop.gold_override(9999)
        shop.edit_shop([["horse",1,1],["pig",1,1],["pig",1,1],["pig",1,1]]) ## another is buffed
        shop.buy(0,4)   
        shop.buy(1,2)
        shop.buy(1,3)
        shop.buy(0,1)   
        # 
        total_hp =battle_phase(board,board, 1) 
        self.assertEqual(total_hp,[3,5],"horse ability failed")
    def test_beaver_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
    
        shop.edit_shop([["beaver",1,1],["beaver",1,1],["beaver",1,1]])
 
        shop.buy(0,4)
        shop.buy(1,2)
        shop.buy(0,1)    
        shop.selling(4)
        self.assertEqual(board.total_of_hp_and_damage_prebattle(),[4,2],"Beaver  test failed")
    def test_pig_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.edit_shop([["pig",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)
        shop.selling(4)
        self.assertEqual(shop.gold,9,"Pig test failed")
    def test_cricket_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
            
        shop.edit_shop([["cricket",1,1],["beaver",1,1],["beaver",1,1]])
        
        shop.buy(0,4)

        total_hp =battle_phase(board,board, 1)
        self.assertEqual(total_hp,[1,1],"failed cricket test")
    def test_mouse_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)


        shop.edit_shop([["mouse",1,1],["beaver",1,1],["beaver",1,1]])
        
        shop.buy(0,4)
        # shop.selling(4)
        # board.position_unit_dict[4].increase_level(3) #testing level 3 just in case they all work the same either way 
        shop.selling(4)
        shop.buy(1,4)
        item_shop.show_items()
        item_shop.buy(1,4)
        total_hp =board.total_of_hp_and_damage_prebattle()
        self.assertEqual(total_hp,[2,2],"failed mouse test")
    def test_honey(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)

        shop.gold_override(9999)

        shop.edit_shop([["horse",1,1],["pig",2,2]])
        
        shop.buy(0,1)
        shop.buy(0,4)
        item_shop.show_items()
        item_shop.edit_shop(["honey"])
        item_shop.buy(0,1)

        total_hp =battle_phase(board,board,1,6)   
        self.assertEqual(total_hp,[3,4],"failed honey test") 
    def test_swan_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        shop.edit_shop([["swan",1,1],["pig",1,1],["mosqutio",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        
        self.assertEqual(board.shop.gold,2,"failed swan test") 
    def test_turkey_abitlity(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
                # shop.reroll()
                ### TODO perma buffs aren't removed when adding units 
        shop.gold_override(9999)
        shop.edit_shop([["turkey",1,1],["pig",1,1],["pig",1,1],["pig",1,1]]) ## another is buffed
        shop.buy(0,4)   
        shop.buy(1,2)
        shop.buy(1,3)
        shop.buy(0,1)   
                # 
        total_hp =battle_phase(board,board, 1) 
        self.assertEqual(total_hp,[7,9],"failed honey test") 
    def test_hedgehog_ability(self):
                
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        shop.edit_shop([["pig",1,91],["pig",1,1],["hedgehog",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
  
        total_hp =battle_phase(board,board, 1,"visable") 
        self.assertEqual(total_hp, [1, 87],"failed hedgehog test") 
    def test_crab_ability(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        # shop.reroll()
        shop.edit_shop([["swan",1,91],["crab",1,1],["pig",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        # board.shop.gold_check()
        total_hp =battle_phase(board,board, "start",1) 
        self.assertEqual(total_hp,[3, 137.5],"failed crab test") 
    def test_snail_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
        # shop.reroll()
        shop.edit_shop([["snail",1,1],["pig",1,1],["hedgehog",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        # board.shop.gold_check()
        total_hp =battle_phase(board,board, "start","visable") 
        self.assertEqual(total_hp,[3, 5],"failed crab test") 
    def test_rat_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
        # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["rat",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        # board.shop.gold_check()
        total_hp =battle_phase(board,board, 1,"visable") 
        self.assertEqual(total_hp,[3, 3],"failed crab test") 
    def test_kangaroo_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
        # shop.reroll()
        shop.edit_shop([["pig",1,1],["kangaroo",1,1],["rat",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 2,"visable") 
        # print(total_hp,"tot")
        self.assertEqual(total_hp,[4, 4],"failed kangaroo test") 
    def test_peacock_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
        # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["peacock",1,9]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 2,"visable") 
        self.assertEqual(total_hp,[11,5],"failed crab test") 
    def test_flamingo_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
        # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["flamingo",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable") 
        self.assertEqual(total_hp,[4,4],"failed flamingo test") 
    def test_sheep_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        
        shop.generate_units()
        board.last_round_lost = True
        shop.gold_override(99999999)
        shop.edit_shop([["pig",1,1],["pig",1,1],["sheep",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   



                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable") 
        self.assertEqual(total_hp,[6,6],"failed sheep test") 
    def test_dodo_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        
        shop.generate_units()
        board.last_round_lost = True
        shop.gold_override(99999999)
        shop.edit_shop([["pig",1,1],["dodo",1,1],["pig",1,1]])
        shop.buy(0,4)
        shop.buy(1,1)
        shop.buy(0,3)   



                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable") 
        self.assertEqual(total_hp,[2,2.5],"failed dodo test")
    def test_dolphin_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
                # shop.reroll()
        shop.edit_shop([["pig",1,5],["pig",1,5],["dolphin",1,5]])
        shop.buy(0,4)   
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable")
        self.assertEqual(total_hp,[3,11],"failed dolphin test")
    def test_giraffe_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
                # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["giraffe",1,1]])
        shop.buy(0,4)   
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable")
        self.assertEqual(total_hp,[3,3],"failed giraffe test")
    def test_dog_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        board.last_round_lost = True
                # shop.reroll()
        shop.edit_shop([["sheep",1,1],["sheep",1,1],["dog",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 10,"visable")
        
        self.assertEqual(total_hp,[15,10],"failed dog test")
    def test_badger_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        board.last_round_lost = True
                # shop.reroll()
        shop.edit_shop([["pig",1,2],["badger",1,1],["pig",1,2]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
                # board.shop.gold_check()#

        board2 = Board()

        shop2= Unit_store()
        board2.shop_linking(shop2)
        shop2.link_to_board(board2)   
        shop2.generate_units()

                # shop.reroll()
        shop2.edit_shop([["dolphin",1,1],["pig",1,2],["pig",1,2]])
        shop2.buy(0,4)  
        shop2.buy(1,1)
        shop2.buy(0,3)   


        # board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board2, 2,"visable")
        print(total_hp)
    def test_elephent_camel_combo(self):
        board = Board()
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        board.last_round_lost = True
        shop.edit_shop([["elephant",1,9],["camel",1,9],["pig",1,9]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 10,"visable")
        self.assertEqual(total_hp,[19,27],"failed giraffe test")
    def test_rabbit_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True
                # shop.reroll()
        shop.edit_shop([["pig",1,1],["rabbit",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   

        item_shop.edit_shop(["apple"])

        item_shop.buy(0,1)
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 2,"visable")
    def test_melon_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True
                # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   

        item_shop.edit_shop(["melon"])

        item_shop.buy(0,4)
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 3,"visable")
        self.assertEqual(total_hp,[1,1],"failed melon test")
    def test_ox_ability(self):
                
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["ox",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   



        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 3,"visable")    
    def test_badger_ability(self):
        
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                # shop.reroll()
        shop.edit_shop([["badger",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   



        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 3,"visable")
        self.assertEqual(total_hp,[1,1],"failed badger test")
    def test_shunk_ability(self):
        
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                # shop.reroll()
        shop.edit_shop([["shunk",1,1],["pig",1,100],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   



        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 3,"visable")
        self.assertEqual(total_hp,[2,66],"failed shunk test")
    def test_hippo_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                # shop.reroll()
        shop.edit_shop([["hippo",1,2],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   

        board2 = Board()

        shop2= Unit_store()
        board2.shop_linking(shop2)
        shop2.link_to_board(board2)   
        shop2.generate_units()

                # shop.reroll()
        shop2.edit_shop([["pig",1,1],["pig",1,1],["pig",1,1]])
        shop2.buy(0,4)  
        shop2.buy(1,1)
        shop2.buy(0,3)   

        total_hp =battle_phase(board,board2, 2,"visable")
        self.assertEqual(total_hp,[5,4],"failed hippo test")
    def test_bison_ability(self):
        board = Board()

        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
                        # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["bison",1,1]])
        shop.gold_override(9999)
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)  
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)  
        shop.buy(0,2)  
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
                        # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable")
        self.assertEqual(total_hp,[11,10],"failed bison test")
    def test_turtle_ability(self):
          
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                        # shop.reroll()
        shop.edit_shop([["turtle",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   



        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 3,"visable")
        self.assertEqual(total_hp,[1,1],"failed turtle test")

    def test_squirrel_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                        # shop.reroll()
        shop.edit_shop([["squirrel",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(1,1)
        shop.buy(0,3)   
        shop.link_item_shop(item_shop)
        item_shop.show_items()
        board.start_of_turn_for_units()

       
        self.assertEqual(item_shop.item_list[0].cost,2,"failed squirrel test")
    def test_penguin_ability(self):
        shop= Unit_store()
        board.shop_linking(shop)
        shop.link_to_board(board)
        shop.generate_units()
        board.last_round_lost = True
                                # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["pig",1,1],["penguin",1,1]])
        shop.gold_override(9999)
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)  
        shop.buy(0,1)   
        shop.buy(0,1)   
        shop.buy(0,1)  
        shop.buy(0,2)  
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
                                # board.shop.gold_check()#
        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable")      
        self.assertEqual(total_hp,[11,11],"failed penguin test")
    def test_whale_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                                # shop.reroll()
        shop.edit_shop([["cricket",1,1],["turkey",1,1],["whale",1,1]])
        shop.buy(0,4)  
        shop.buy(0,1)
        shop.buy(0,3)   



        board_2 = copy.deepcopy(board)
        total_hp =battle_phase(board,board_2, 1,"visable")
    # def test_parrot_ability(self):
    # def test_rhino_ability(self):
    def test_monkey_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                                # shop.reroll()
        shop.edit_shop([["monkey",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(0,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()

        board_2 = copy.deepcopy(board)
        # board_2.position_unit_dict[4] = Unit("pig",1,19)
        total_hp =battle_phase(board,board_2, 3,"visable")
        self.assertEqual(total_hp,[5,6],"failed monkey test")
    def test_scorpion_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                                # shop.reroll()
        shop.edit_shop([["scorpion",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(0,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()

        board_2 = copy.deepcopy(board)
        board_2.position_unit_dict[4] = Unit("pig",1,19)
        board_2.position_unit_dict[4].buff_perk("peanut")
        total_hp =battle_phase(board,board_2, 1,"visable")
    def test_crocodile_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                                # shop.reroll()
        shop.edit_shop([["crocodile",1,1],["pig",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(0,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()

        board_2 = copy.deepcopy(board)
        # board_2.position_unit_dict[4] = Unit("pig",1,19)
        # board_2.position_unit_dict[4].buff_perk("peanut")
        total_hp =battle_phase(board,board_2, 1,"visable")
    def test_seal_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.link_item_shop(item_shop)
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                                # shop.reroll()
        shop.edit_shop([["cow",1,1],["seal",1,1],["pig",1,1]])
        shop.buy(0,4)  
        shop.buy(0,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
        item_shop.show_items()
        board_2 = copy.deepcopy(board)
        item_shop.buy(0,1)
    def test_shark_ability(self):
        board = Board()
        shop= Unit_store()
        item_shop= Item_shop(shop)
        board.shop_linking(shop)
        shop.link_to_board(board)   
        shop.link_item_shop(item_shop)
        shop.generate_units()
        shop.gold_override(9999)
        board.last_round_lost = True    
                                # shop.reroll()
        shop.edit_shop([["pig",1,1],["pig",1,1],["shark",1,1]])
        shop.buy(0,4)  
        shop.buy(0,1)
        shop.buy(0,3)   
        board.start_of_turn_for_units()
        board.end_of_turn_for_units()
        item_shop.show_items()
        board_2 = copy.deepcopy(board)

        # board_2.position_unit_dict[4] = Unit("pig",1,19)
        # board_2.position_unit_dict[4].buff_perk("peanut")
        total_hp =battle_phase(board,board_2, 1,"visable")
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