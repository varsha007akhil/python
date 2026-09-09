rice_price = 45
sugar_price = 40
oil_price = 130

rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

total_rice = rice_price*rice_quantity
total_sugar = sugar_price*sugar_quantity
total_oil= oil_price*oil_quantity

print("rice_total:",total_rice)
print("sugar_total:",total_sugar)
print("oil_total:",total_oil)

total_bill = total_rice + total_sugar +total_oil
print("total_bill:",total_bill)

integer_bill = int(total_bill)
print("Integer bill:", integer_bill)


string_bill = str(total_bill)
print("String bill:", string_bill)


import random
delivery_charge = random.randint(5, 10)
print("Delivery charge:", delivery_charge)


final_bill = total_bill + delivery_charge
print("Final bill:", final_bill)