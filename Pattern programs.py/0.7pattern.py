#####
'''''
programe output--->>>
1
21
321
4321
54321

'''''
#####

row =int(input("Enter row value:"))
for i in range(row):
    for j in range(i+1,0,-1):
        print(j,end="")
    print()