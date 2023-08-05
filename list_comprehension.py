fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

list = [a for a in range(10)]

print(list)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)