numbers = list(map(int, input("Enter elements of first array with space :").split()))
num = int(input("Enter the number which occurance to be find : "))
if num in numbers:
    print(f"{num} is present {numbers.count(num)} times in array")
else:
    print(f"{num} not present in array")
arr1 = list(range(1, 10))
arr2 = list(range(9, 0, -1))
# arr3 = arr1.copy()
# arr3.sort(reverse=True)
print(arr1)
print(arr2)
# print(arr3)
for num in range(len(arr1)):
    if arr1[num] == 5:
        print(arr1[num], "=", arr2[num], "=", arr1[num]+arr2[num])
    print(arr1[num], "+", arr2[num], "=", arr1[num]+arr2[num])
