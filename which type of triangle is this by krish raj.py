print ("this program is made by Krish Raj")
print ("this program is made for enter side and find which type of triangle is this")

a = int(input(" enter the first side of triangle : "))
b = int(input(" enter the second side of triangle : "))
c = int(input(" enter the third side of triangle : "))
d = a**2
e = b**2
f = c**2

if a==b and b==c and a==c :
  print (" this is equilateral triangle ")
if a==b and a!=c or b==c and b!=a or a==c and a!=b :
 print (" this is isosceles triangle ")
if a!=b and b!=c and c!=a :
  print (" this is scalene triangle ")
if (d+e)==f or (e+f)==d or (d+f)==e :
  print ("this is also right angle triangle")

print "Thankyou for using this program "
print ("BYE BYE BYE")
