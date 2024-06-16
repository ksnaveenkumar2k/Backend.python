#####
'''''
programe output--->>>
1
12
123
1234
12345
'''''
#####

row = int(input("Enter row value:"))
for i in range(row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
