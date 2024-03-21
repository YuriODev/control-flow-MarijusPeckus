# Your solution to Exercise 14
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
x = False
if a == d:
  if b ==c :
    x = True
else:
  x = False
if x == True:
  print()
