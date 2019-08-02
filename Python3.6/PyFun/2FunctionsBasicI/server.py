#def a():
#    return 5 #hands back a value of 5 to a()
#print(a())     #Prints a string with the value 5 within it

#def a():
#    return 5 #hands back a value of 5 
#print(a()+a())     #Prints a string of integers that equals out to 10

#def a():
#    return 5   #hands back a value of 5
#    return 10   #a value has already filled it
#print(a())     #prints a value of 5

#def a():
#    return 5 #hands back a value of 5
#    print(10) # prints nothing
#print(a())     # prints the value of 5 within it

#def a():
#    print(5)    #Tries to give a() a print value of 5
#x = a()         #turns x into the value of a(5, none)
#print(x)     

#def a(b,c):        #defines a() with the parameters of b,c
#    print(b+c)     #attempts to give a print value of b+c which is yet to be defined
#print(a(1,2) + a(2,3))  #should attempt to add 1+2 and 2+3 followed by those two final numbers together, after running it appears to have an error though

#def a(b,c):
#    return str(b)+str(c) #gives a return value of a string to b and c 
#print(a(2,5))      prints out to 25

#def a():           
#    b = 100    # sets value to 100
#    print(b)   # prints 100
#    if b < 10:     
#        return 5
#    else:
#        return 10
#    return 7
#print(a())         #prints out to 10

#def a(b,c):
#    if b<c:
#        return 7
#    else:
#        return 14
#    return 3
#print(a(2,3))
#print(a(5,3))
#print(a(2,3) + a(5,3))     #prints 7, 14, 21. Had a lot of trouble with his

#def a(b,c):
#    return b+c
#    return 10
#print(a(3,5))     #returns a value of 8
#b = 500
#print(b)       #returns a value of 500

#def a():       #b isnt defined so the code will break
#    b = 300
#    print(b)
#print(b)
#a()
#print(b)  
#b = 500
#print(b)

#def a():       #b isnt defined so the code breaks
#    b = 300
#    print(b)
#    return b
#print(b)
#a()
#print(b)  
#b = 500
#print(b)

#def a():       #b isn't defined so it shouldnt print or return anything
#    b = 300
#    print(b)
#    return b
#print(b)
#b=a()
#print(b)
#____________________________________________________
#def a():       #prints 1, 3, then 2
#    print(1)
#    b()
#    print(2)
#def b():
#    print(3)
#a()
#____________________________________________________________________
#def a():
#    print(1)
#    x = b()
#    print(x)
#    return 10     

#def b():            
#    print(3)
#    return 5
#y = a()
#print(y)        #returns value of 1, 3, 5, then 10