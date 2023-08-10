thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple_1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple_1)
print(len(thistuple_1))
print(thistuple[1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


fruits_1 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits_1

print(green)
print(tropic)
print(red)
thistuplef = ("apple", "banana", "cherry")
for a in thistuplef:
  print(a)