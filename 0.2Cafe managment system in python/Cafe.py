# Define menu of Restaurant
menu ={
    "tea":30,
    'greentea':40,
    'coffee':50,
    'soda':50,
    'salad':60,
    'pizza':80,
    'pasta':100,
    'burger':110,
    'sandwiches':120,
    'chicken':130,
    'fish':150,
} 
cart=[]
total= 0
#Greating
print(">>>>  Welcome to CODERS_CABIN Restaurant  <<<<")
print("--------Menu----------")
for key, value in menu.items():
    print(f"{key:12}: Rs{value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit):").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------YOUR ORDER------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: Rs{total:.2f}")
print("Thank you for choosing our restaurant. It was a pleasure preparing your order...!!!")
        