#####
'''''
row=int(input(3))

programe output--->>>
1
2  3  
4  5  6  
7  8  9 10

'''''
#####
row =int(input("Enter row value:"))
num=1
for i in range(row+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print("\n")