list1 = []
list2 = []
common_values = []
for i in range(3):
    number1 = int(input('Enter Elemets for Array 1 : '))
    list1.append(number1)
    number2 = int(input('Enter Elemets for Array 2 : '))
    list2.append(number2)
for value in list1:
    if value in list2:
        common_values.append(value)
l1 = list(set(list2)-set(list1))
l2 = list(set(list1) - set(list2))
uncommon_values = l1+l2

print(list1)
print(list2)
print(common_values)
print(uncommon_values)