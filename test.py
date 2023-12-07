


# dice_art = ["""
#  -------
# | Damage   hp   |
# |   UN   |
# |       |
#  ------- ""","""
#  -------
# |       |
# |   1   |
# |       |
#  ------- """]

# base_upper=" ---------"
# base_upo_middle = " |   P   |"
# base_middle = " |   N   |"
# base_low_middle = " |  d  h  |"
# base_lower=" ---------"

# #use this code just format it better
# player = [0, 1]
# lines = [dice_art[i].splitlines() for i in player]
# for l in zip(*lines):
#     print(*l, sep='')
# import numpy as np 
# cjhec = ["a","b","c"]
# list_ally_index = np.random.choice(cjhec, size=2, replace=False)
indexsel
# print(list_ally_index)

           if self.position_unit_dict[end].Name  == self.position_unit_dict[origin].Name and not self.position_unit_dict[end].level == 3:
                # self.position_unit_dict[place].Name == self.shop_units[index].Name and not self.shop_units[index].level == 3:
                print("LEVELING UP ")
                self.position_unit_dict[end].level_amount = self.board.position_unit_dict[origin].level_amount  +self.position_unit_dict[end].level_amount +1
                self.position_unit_dict[end].perma_buff(self.position_unit_dict[origin],self.position_unit_dict[end])
                
                if self.position_unit_dict[origin].level == 1 and self.board.position_unit_dict[origin].level_amount ==2 :
                    
                    self.position_unit_dict[origin].update_state("level_up")
                    self.position_unit_dict[origin].update()
                    self.position_unit_dict[origin].level = self.board.position_unit_dict[origin].level+1

                    self.position_unit_dict[origin].level_amount =self.board.position_unit_dict[origin].level_amount - 2

                if self.position_unit_dict[origin].level == 2 and self.board.position_unit_dict[origin].level_amount >2:
                    self.position_unit_dict[origin].update_state("level_up")
                    self.position_unit_dict[origin].update()
                    self.position_unit_dict[origin].level_amount =self.board.position_unit_dict[origin].level_amount - 3
                    self.position_unit_dict[origin].level = self.board.position_unit_dict[origin].level+1


                    elif  self.position_unit_dict[end].Name == self.position_unit_dict[origin].Name and not self.position_unit_dict[origin].level == 3:
             print("LEVELING UP ")
             self.position_unit_dict[end].level_amount = self.position_unit_dict[end].level_amount  +self.position_unit_dict[origin].level_amount +1
             self.position_unit_dict[end].perma_buff(self.position_unit_dict[origin].level,self.position_unit_dict[origin].level)

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


            #  elif  self.board.position_unit_dict[place].Name == self.shop_units[index].Name and not self.shop_units[index].level == 3:
            #  print("LEVELING UP ")
            #  self.board.position_unit_dict[place].level_amount = self.board.position_unit_dict[place].level_amount  +self.shop_units[index].level_amount +1
            #  self.board.position_unit_dict[place].perma_buff(self.shop_units[index].level,self.shop_units[index].level)

            #  if self.board.position_unit_dict[place].level == 1 and self.board.position_unit_dict[place].level_amount ==2 :
            #      print("LEVEL 2 ")
            #      self.board.position_unit_dict[place].update_state("level_up")
            #      self.board.position_unit_dict[place].update(self.board)
            #      self.board.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1

            #      self.board.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 2

            #  if self.board.position_unit_dict[place].level == 2 and self.board.position_unit_dict[place].level_amount >2:
            #      self.board.position_unit_dict[place].update_state("level_up")
            #      self.board.position_unit_dict[place].update()
            #      self.board.position_unit_dict[place].level_amount =self.board.position_unit_dict[place].level_amount - 3
            #      self.board.position_unit_dict[place].level = self.board.position_unit_dict[place].level+1