list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_number=list_numbers[0]
index=0
for pos,val in enumerate(list_numbers):
    if val > max_number:
        max_number=val
        index=pos
list_numbers[index],list_numbers[19]=list_numbers[19],list_numbers[index]
# TODO Оформить решение

print(list_numbers)
