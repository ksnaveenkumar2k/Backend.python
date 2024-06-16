############
'''''
programe output--->>>
*
**
***
****
*****
******
*******
********
*********
**********
'''''
############

row =int(input("Enter row value:"))
for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()
        
