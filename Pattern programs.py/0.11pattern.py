#####
'''''
row=int(input(5))

programe output--->>>
1
1 2 1
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1

'''''
#####
row =int(input("Enter row value:"))
for i in range(row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(j,0,-1):
        print(k,end=" ")
    print("\n")