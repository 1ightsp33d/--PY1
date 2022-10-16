list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
MAX_I=0
for i in range(len(list_numbers)):
    if list_numbers[i]>list_numbers[MAX_I]:
        MAX_I=i

list_numbers[-1],list_numbers[MAX_I]=list_numbers[MAX_I],list_numbers[-1]
# TODO Оформить решение

print(list_numbers)
