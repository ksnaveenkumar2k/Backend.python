######
''''
a =input("Enter a string:")
total =0
for i in (a):
    if i.isdigit():
        total = total+int(i)
print("sum of all integers in string:",total)
'''
######
def find_sum(a):
    num =0
    sum =0
    for i in (a):
        if i.isdigit():
            num =num*10+int(i)
        else:
            sum =sum+num
            num =0
    return sum+num
a =input("enter any string:")
print(find_sum(a))


