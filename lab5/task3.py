import random
def get_unique_list_numbers() -> list[int]:
 a=set();
 while len(a)<10:
     a.add(random.randint(-10,10))
 return list(a)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
