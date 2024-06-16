#####
'''''

          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *

'''''
#####
row =int(input())
for i in range(1,row):
    for j in range(6,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print("\n")
    