def strings_finder(my_strings):
    for item in my_strings:
        if 'hand' in item:
            return True
    return False


my_strings = ["put your hands on the table"]
result = strings_finder(my_strings)
print(f"В списку задане слово: {result}")

my_strings = ["somethink on the table"]
result = strings_finder(my_strings)
print(f"В списку задане слово: {result}")