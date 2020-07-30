shopping_list = ["milk","eggs","pasta","spam","bread","rice"]

# for item in shopping_list:
#     if 'spam' == item:
#         break
#     print("Buy "+item)

item_to_find='spam'
found_at=None
# print(len(shopping_list))
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         print(f"it is found on postion {index+1}")
#         break
if item_to_find in shopping_list:
    found_at=shopping_list.index(item_to_find)
print(found_at)