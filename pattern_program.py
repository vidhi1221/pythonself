
print("pattern_no 1")
for i in range(1,4):
    for j in range(1,4):
        print('*',end=" ")
    print()
print("========================================")
print("pattern_no 2")
for i in range(1,4):
    for j in range(i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 3")
for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()
print("========================================")
print("pattern_no 4")
for i in range(1,5):
    for j in range(0,i):
        print(i,end=" ")
    print()
print("========================================")
print("pattern_no 4")
n=1
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()
print("========================================")
print("pattern_no 5")
n=1
for i in range(1,5):
    for j in range(1,i+1):
        print(n**2,end=" ")
        n+=1
    print()
print("========================================")
print("pattern_no 6")
n=ord("A")
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n+=1
    print()
print("========================================")
print("pattern_no 7")
n=ord("A")
for i in range(1,5):
    for j in range(i):
        print(chr(n),end=" ")
    n+=1
    print()
print("========================================")
print("pattern_no 8")
for i in range(1,5):
    n=ord("A")
    for j in range(i):
        print(chr(n),end=" ")
        n+=1
    print()
print("========================================")
print("pattern_no 9")
for i in range(1,5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 10")
for i in range(1,5):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 11")
for i in range(1,5):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 11")
for i in range(4,0,-1):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 12")
for i in range(1,5):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 13")
for i in range(1,5):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 14")
for i in range(4,0,-1):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
print("========================================")
print("pattern_no 15")
for i in range(4,0,-1):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(2,5):
    for space in range(4,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()