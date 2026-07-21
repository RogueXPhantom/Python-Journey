# Have to use same  name twise 
dict = {}

name = input("Enter Friend's name: ")
language = input("Enter Fav Language: ")

dict.update({name:language})

name = input("Enter Friend's name: ")
language = input("Enter Fav Language: ")

dict.update({name:language})

name = input("Enter Friend's name: ")
language = input("Enter Fav Language: ")

dict.update({name:language})

name = input("Enter Friend's name: ")
language = input("Enter Fav Language: ")

dict.update({name:language})

print(dict) # name will register once with last input bcs we have used "update" here 
