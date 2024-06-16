prinicpal =int(input())
rate =int(input())
years =int(input())
interest =(prinicpal*rate*years)/100.0
amount =(prinicpal+interest)
discount =(2*interest)/100.0
final_settlement =(amount-discount)
print("%.2f"%interest)
print("%.2f"%amount)
print("%.2f"%discount)
print("%.2f"%final_settlement)

