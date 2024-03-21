# Your solution to Exercise 13
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
x = False
if a != b or a != c or a != d or b != c or b != d or c != d :
  x =True
if x == True
    print()