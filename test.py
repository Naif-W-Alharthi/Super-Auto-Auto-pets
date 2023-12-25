test_list = [1, 4, 2, 9, 8]
 
# print(test_list[-1])
last_unit = None
target = 8
target_unit = None
    # print(id(owner_board),"OWNER BOARD BY FUNCTRION")
    # print(id(camel.owner_board),"OWNER BORAD BY UNIT")
for index,unit in enumerate(test_list):
        

        if unit == target:
            if index+1 > len(test_list):
                  test_list[index + 1] = test_list[index + 1] +222
            # if index +1<= len(test_list):
            #       test_list[index - 1] = test_list[index + 1] +222
        # if target_unit != None and last_unit != None :
        #     test_list[last_unit]= test_list[last_unit] +92
        #     test_list[index] = test_list[index] +123
        #     print(last_unit,target_unit,index,"indexs")
        #     break
        # elif unit!= target:
        #      last_unit = index
        #      print(last_unit,"last unit")
        # else:
        # # if unit == target:
        #       target_unit= index
        #       print(target_unit,"target_unit")
            #  print("buffed ",owner_board.order[last_index].Name)
      

print(test_list)


# before_unit= None
#     badger_unit=  None
#     print(prior_list)
#     for unit in prior_list:
#         print(unit.Name,"badger unit name")
#         print(before_unit,badger_unit,unit.Name,"YYYY")
#         if badger_unit != None and before_unit != None:
#             unit.take_damage(badger.Base_damage)
#             before_unit.take_damage(badger.Base_damage)
#             print("dealt damage")
#             # unit.take_damage(badger.Base_damage)
#         if unit !=badger:
#             before_unit = unit
#             print("not badger damage")
#         if unit == badger:
#             badger_unit = unit
#             print("found badger")


# # printing original list
# print("The original list is : " + str(test_list))
 
# # declaring elements till which elements required
# N = 4
 
# # Get elements till particular element in list
# # using index() + list slicing
# temp = test_list.index(N)
# res = test_list[temp:]
# # rest = res[2:]
# # printing result
# print("Elements till N in list are : " + str(res))