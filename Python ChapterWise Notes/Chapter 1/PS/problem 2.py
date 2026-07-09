import os

# Add the directory path of what files you wanna know about 
# here "directory_path" and "directory" both works same 
directory_path = "/"

# this uses the os module to list the directory contents 
contents = os.listdir(directory_path)

# this prints the contents of directory given there
print(contents)