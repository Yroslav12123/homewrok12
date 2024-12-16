def strings_longer_than_ten(my_strings):
    for hand in my_strings:
     if hand in my_strings:
         return  True
     return  False





my_strings = ["put your hand on the table"]
result = strings_longer_than_ten(my_strings)
print(f"В списку знайдено задане слово: {result}")
