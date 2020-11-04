print ( " This program is made by Krish Raj " )
print ( " This program is made for student to give fine for return book late " )
a = int(input( " Enter the number of days the member is late to return the book  : " ))
if a < 5 or a == 5 :
    print  " You give " + str (a) + " days late to return the book , The fine is 50 paise " 
if a < 10 and a > 5 or a == 10 :
    print " You give " + str (a) + " days late to return the book , The fine : 1 rupee " 
if  a < 30 and a > 10 or a == 30 :
    print  " You give " +str (a) + " days late to return the book , The fine : 5 rupee " 
if a > 30 :
    print  " Your membership will be cancelled " 
print " Thank You for use this program "
