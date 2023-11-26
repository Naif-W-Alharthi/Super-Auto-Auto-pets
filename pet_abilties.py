

from main import Unit # add more as time goes on    

def otter_ability(otter,shop_board):

    for k in shop_board.random_n_amount_of_units(otter.level):

        k.perma_buff(0,1) 
        print("otter ability worked")
    ##when bought give random ally +1*lvl hp 
    
def mosquito_ability(self,owner_board):

  
        target_unit =owner_board.enemy_board.random_single_unit()
        target_unit.take_damage(self.level)
        print(target_unit.Name, "took damage mosquito ")
        owner_board.enemy_board.remove_fainted_list()
        owner_board.remove_fainted_list()
    

def ant_ability(self,owner_board=None):
   
        buff_amount = self.level
        self.owner_board.random_single_unit().temp_buff(buff_amount,buff_amount)
        

def rat_ability(self,shop_board):
    shop_board.append()
def duck_ability(duck,shop_board):
    for unit in shop_board.shop_units:
        unit.perma_buff(0,duck.level)
        print("duck buffed" ,unit.Name)


def beaver_ability(beaver,shop_board):
   for k in shop_board.random_n_amount_of_units(2):

        k.perma_buff(beaver.level,0) 
   
def cricket_ability(cricket,player_board):
    player_board.insert(0,Unit("zombiecircket",1,1))# add it at the start of line in combat 

def fish_ability(fish,player_board): 
       for units in player_board.random_n_amount_of_units(2):

        units.perma_buff(fish.level,fish.level) 