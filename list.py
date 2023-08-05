myList = ["apple","banana","cherry"]
print(myList)
print(len(myList))
#access list
myList = ["apple", "banana", "cherry","orange","kiwi","melon","mango"]
print(myList[1])
print(myList[2:5])
print(myList[:4])
print(myList[2:])
tropical = ["mango", "pineapple", "papaya"]
myList.extend(tropical)
print(myList)
newList = ["apple", "banana", "cherry"]
for x in newList:
  print(x)
  lastlist = ["apple", "banana", "cherry"]
i = 0
while i < len(lastlist):
  print(lastlist[i])
  i = i + 1