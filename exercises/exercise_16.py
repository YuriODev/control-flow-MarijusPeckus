# Your solution to Exercise 16
day = int(input())
month = int(input())
year = int(input())
leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
  if day == 1:
    day = 31
    month -= 1
  elif day < 31:
    day -= 1
  else:
    print()
elif month == 4 or month == 6 or month == 9 or month == 11:
  if day == 1:
    day = 30
    month -= 1 
  elif day <30:
    day -= 1
  else:
    print()
elif month == 2:
  if day == 29:
    if leap == True:
      day = 28
      month -= 1
    elif day < 29:
      day -= 1
    else:
      print()
    if leap == False:
      if day == 28:
        day = 27
        month -= 1
      elif day < 28:
        day -= 1
      else:
        print()
if month == 1 and day == 1:
  year -= 1
  month = 12
  day = 31
print(day".."month".."year")  
  
  



