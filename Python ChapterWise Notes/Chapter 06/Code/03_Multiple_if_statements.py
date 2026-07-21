a =  int(input("Enter Your Age: "))

if(a%2==0):  #this will work independently other than lower one
    print("your age is even")
# End of statement no 1 

if(a>=18):
    print("You're adult")

elif(a<0):
    print("You're entering an invalid age ")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You're minor")
# End of statement no 2

print("End of survey")