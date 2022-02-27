from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, 
you use it by making an instance, or object,of the class. 
You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user.
The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''
print("------------------------ Instance 1 Values for the Arithmetic class--------------------")
ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

print("-------------------------- Instance 2 Values for the Arithmetic class--------------------")
ar2 = Arithmetic()
ar2.__init__(100, 200)
print(ar2.add())
print(ar2.subtract())
print(ar2.multiply())
print(ar2.divide())
print(ar2.remainder())
ar2.print_self()

print("---------------------------- Instance 3 Values for the Arithmetic class------------------------")
ar3 = Arithmetic()
ar3.__init__( 400, 100)
print(ar3.subtract())
print(ar3.multiply())
print(ar3.remainder())
ar3.print_self()

print("--------------------------- Instance 4 Values for the Arithmetic class-------------------------")
ar4 = Arithmetic()
ar4.__init__( 1000, 2000)
print(ar4.add())
print(ar4.subtract())
print(ar4.multiply())
print(ar4.divide())
ar4.print_self()