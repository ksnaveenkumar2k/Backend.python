#####
'''''
row=int(input(4))

programe output--->>>
1
2  3  4
5  6  7  8  9
10 11 12 13 14 15

'''''
#####

row = int(input("Enter row value:"))
c =1
n =1
for i in range(1,row+1):
    for j in range(1,c+1):
        print(n,end=" ")
        n=n+1
    c=c+2
    print('\n')
    