print("<<<<--Welcome to Naveen Bank-->>>>\n  To Your Trust Bank of India\n\nInsert your ATM card")

password =1234
balance =50000.0
choice =0

pin =int(input("Enter your four digit pin:"))

if (pin==password):
    
    while choice !=4:
        
      print("\n\n<<---Menu--->>")
      print("1|== balance")
      print("2|== deposite")
      print("3|== withdraw")
      print("4|== cancel")
      
      choice=int(input("\nEnter your option:"))
      
      if (choice==1):
          print("Balance =Rs",balance)
          
      elif (choice==2):
          dep=float(input("Enter your deposit:Rs"))
          balance +=dep
          print("\nDeposited amount:Rs",dep)
          print("Balance =Rs",balance)
          
      elif(choice==3):
          wit=float(input("Enter your amount to withdraw:Rs"))
          balance -=wit
          print("\nWithdraw amount:Rs",wit)
          print("Balance =Rs",balance)
          
      elif(choice==4): 
          print("\n      Thank You\nFor Visting Our ATM\nCash is the most widely accepted payment type in the world.!!!")
          
      else:
          print("\nInvalid Entry!!!")
else:
    
    print("Pin incorrect !!! Try again")
    
