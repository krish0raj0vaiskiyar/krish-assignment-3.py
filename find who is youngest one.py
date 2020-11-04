print (" this program is made by KRISH Raj ")
print ("this program is made for tell who is youngest one")
a = int(input("enter the age of Ram : "))
b = int(input("enter the age of Shyam : "))
c = int(input("enter the age of Ajay : "))
        
if a<b and a<c :
  print ("Ram is youngest one ")
if b<c and b<a :
  print ("Shyam is youngest one ")
if c<a and c<b :
  print ("Ajay is youngest")
if a==b and a!=c :
  print ("Ram and Shyam are of the same age")
if b==c and b!=a:
  print ("Shyam and Ajay are of the same age")
if a==c and a!=b :
  print ("Ram and Ajay are of the same age")
if a==b and b==c :
  print ("all are of the same age")
