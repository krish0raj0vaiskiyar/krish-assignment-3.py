print ("this program is made by Krish Raj")
print ("this program is made for verify side of triangle")
a = int(input(" enter the first side of triangle : "))
b = int(input(" enter the second side of triangle : "))
c = int(input(" enter the third side of triangle : "))

if (a+b)>c and (b+c)>a and (a+b)>c :
  print ( " Yes they are side of triangle " )
else :
  print ( " They are not side of triangle " )
