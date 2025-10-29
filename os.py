# os:- operating system interface, intract with the operating system

ex:- managing files, directories and environment varialbles


# working with directories
import os
print(os.getcwd())
os.mkdir('new_folder')
print(os.listdir())
os.rmdir('new_folder')


#path operations
import os
path = "/home/user/documents/file.txt"

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.exists(path))



#Run os commands
import os
os.system("echo hello from phthon!")

o/p:- hello from python



