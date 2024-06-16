#####
'''''
programe output--->>>
54321
4321
321
21
1
'''''
#####

row =int(input("Enter row number:"))
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()