# Loops in python

# What is loop
    # With the help of loop we can print or execute particular part or statement multiple time based on the true or false condition
    # In python there is two types of loops
        # for loop
        # while loop

# while loop : -
    # while loop is used for infinite loop : means when we have to excute particular part infinite time (continue loop)
    # in this when you give any condition in while loop and thats true or false it will print that statement 
        # again and again. 
    # if we get condition false it will stop execution
 
a = 0
while a <= 10:
    print(a)
    a+=1

# for loop : -
    # In python for loop work with sequence only. It is a iterable varible
    # we can traversing with object(acces each element) using for loop. 
    # we travers on it one by one (this called iterable object)
    # iterable object automatically visit next element or toward to next element
    # for loop will terminate your program after using or traversing each elements of your sequance
    # we can use directly iterable object either using range function we can give particular range for traversing.

for i in range(1,11):
    print(i)

# nested loop : -
    # it is not a type of our loop it is just a concept of loop 
    # nested loop means loop inside loop 
    # in this first loop represent as row 
        # and second loop represent as coloumn