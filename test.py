
a = ["Python", "Django"]
b = ["Python", "Django"]
c = a

print(a is c)
# returns True because c is the same object as a
print(a is b)
# returns False because a is not the same object as b, even if they have the same content
print(a == b)
# to demonstrate the difference between "is" and "==": this comparison returns True because a is equal to y