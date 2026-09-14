fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "broccoli", "spinach"]
beverages = ["water", "juice", "soda"]

fruits.append("grape")
print(fruits)
vegetables.insert(2,"tomato")
print(vegetables)
beverages.pop()
print(beverages)
inventory = [fruits,vegetables,beverages]
print(inventory)
print(fruits[0:2])
print(vegetables[-1])
length =[len(x) for x in fruits]
print(length)
print("water" in beverages)
tuple = (fruits[0],vegetables[0],beverages[0])
print(tuple)



