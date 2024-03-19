# Your solution to Exercise 8
number = int(input())
digit = int(input())

ifinnumber = digit == number % 10 or digit == (number // 10) % 10 or digit == number // 100

print(ifinnumber)

