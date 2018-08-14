'''
Zach Miller
9/3/13
CIS-127
'''
foodCharge=float(input("Enter the charge for food:"))
tip=(foodCharge*.15)
tax=(foodCharge*.07)
total=(foodCharge+tip+tax)
print('Tip:',format(tip,'.2f'))
print('Tax:',format(tax,'.2f'))
print('Total:',format(total,'.2f'))
