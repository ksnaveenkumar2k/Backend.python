x =int(input())
y =int(input())
sell =12*y
loss=(x-sell)
profit =(sell-x)
if (sell<x):
  print(f"Loss : Rs.{loss}")
elif(x>sell):
  print(f"Profit : Rs.{profit}")
else:
  print("No profit nor loss")