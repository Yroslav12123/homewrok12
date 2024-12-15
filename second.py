def strings_longer_than_ten(my_strings):
    for s in my_strings:
     if len(s) > 10:
         return  True
     return  False





my_strings = ["коротка стрічка", "дуже довга стрічка, набагато довша за 10 символів", "а це коротка"]
result = strings_longer_than_ten(my_strings)
print(f"Список має стрічки довші за 10 символів: {result}")

my_strings = ["маленька", "трохи більша", "ще трохи більша"]
result = strings_longer_than_ten(my_strings)
print(f"Список має стрічки довші за 10 символів: {result}")