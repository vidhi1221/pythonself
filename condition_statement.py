# Condition Statement Or Decision Statemnet 

# Condition statement use to make a decision on evaluation as per the condition 
# it execute true value if condition is true either it will execute false value

# condition statement types 

# if : -
        # if condition block create by using (:) colon.
        # we use expression as a condition
        # if condition is execute when condition is true either it will stop executing the program

# example : -
a = 10
if a>5: # here condition is true thats why if block is print 
    print(a)

b = 20 
if a>b: # here condition is false thats why if block is not print 
    print(b)


# if else : - 
        # else block use when if condition is false then else block will print 

# example : -
a = 10
if a > 20:
    print("a is greater") # here if block is false 
else :
    print("a is less than 20") #thats why else block is print

# nested if : -
        # this condition statement create condition inside condition
        # means if inside if 
        # it will execute when first if condition is true after that i will go inside that if block 
        # either it will go else part if else park is availbe 

# example : -
a = int(input("Enter number here"))
if a > 5:
    if a > 10:
        print("a is greater than 10")
    else:
        print("a is less than 10")
else:
    print("a is less than 5")

# elif : -
        # elif condition is used for when we have to check unlimited condition at one time 
        # it check condition first if that condition is false it will go to next condition for check 
        # it will check condition till get the condition is true 
        # once we get condition is true it stop the execution 
    
a = int(input("Enter number here"))

if a < 5:
    print("a is less than 5")

elif a < 10:
    print("a is less 10")

elif a < 15:
    print("a is less than 15")

elif a < 20:
    print("a is less 20")

else:
    print("a is greter than 20")
