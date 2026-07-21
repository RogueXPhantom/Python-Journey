a =  int(input("Enter Your Age: "))

if(a>=18):
    print("You're adult")

elif(a<0):
    print("You're entering an invalid age ")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You're minor")

print("End of survey")