fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  for a in range(6):
    print(a)
else:
  print("Finally finished!")