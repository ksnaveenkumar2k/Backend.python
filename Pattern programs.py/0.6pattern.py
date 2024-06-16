#####
'''''
programe output--->>>
12345
1234
123
12
1
'''''
#####

row =int(input("Enter row value:"))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
        
    