# Your solution to Exercise 2
age = int(input("Enter the persons age"))
if age <= 1:
  print("the person is an infant")
elif age > 1 and age < 13:
  print("the person is a child")
elif age >= 13 and age < 20:
  print("the person is a teenager")
else:
  print("You are an adult")

