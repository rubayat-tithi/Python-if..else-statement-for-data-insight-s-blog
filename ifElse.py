#If condition checking

a = 10
b = 100
if b > a:
  print("b is greater than a")

#elif keyword is used if the previous statements were false.
c = 20
d = 20
if c > d:
  print("d is greater than c")
elif c == d:
  print("c and d are equal")

#else keyword is used if either of statement is not true
a = 100
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#if we have single conditions to check, we can use ternary operator
a = 200
b = 20

if a > b: print("a is greater than b")

#nested if
x = 100

if x > 10:
  print("x is bove ten,")
  if x >= 40:
    print("x is above or equal to 40!")
  else:
    print("but not above 40.")
