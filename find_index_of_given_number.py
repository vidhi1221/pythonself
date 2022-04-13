array1 = list(map(int, input("Enter elements of first array with space :").split()))
array1 = list(map(int, input("Enter elements of second array with space :").split()))



numbers = list(
    map(int, input("Enter elements of first array with space :").split()))
print(numbers)

num = int(input("Enter Number which want to find : "))
if num in numbers:
    print(f"{num} is present at {numbers.index(num)} postion")
else:
    print(f"{num} not present in array")
