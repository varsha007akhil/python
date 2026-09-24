n = int(input("How many names: "))

try:
    f = open("students.txt", "r")
    print(f.read())
    f.close()
except:
    pass

f = open("students.txt", "a")

for i in range(n):
    name = input("Enter name: ")
    f.write(name + "\n")

f.close()

f = open("students.txt", "r")
print(f.read())
f.close()