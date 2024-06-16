n =int(input())
x =n
sum =0
while x > 0:
    r =x%10
    sum=sum+r
    x=x//10
if (n%sum==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")