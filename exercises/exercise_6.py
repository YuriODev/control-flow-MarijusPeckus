# Your solution to Exercise 6
ax =int(input("enter the x coordinate"))
ay =int(input("enter the y coordinate"))
bx =int(input("enter the x coordinate"))
by =int(input("enter the y coordinate"))

num = ax **2 + ay **2 
num = num ** 1/2
num2 = bx **2 + by **2
num2 = num2 ** 1/2

if num > num2:
  print("point (",ax,",",ay,") is closer to (0,0)"")
else :
  print("point (",bx,",",by,") is closer to (0,0)"")
