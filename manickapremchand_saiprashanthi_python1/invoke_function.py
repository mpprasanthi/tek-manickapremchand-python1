

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values,
or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more
than once, wrap that code in a function and call it when you need it.
When you need to change how the action is carried out, you can change the code in the
function, and the improvement is applied everywhere.
'''

print("---------------Invoking zero arg function--------------")
zero_arg_function()

print("---------------Invoking function with required arguments-----------")
introduction("Harry", "Houdini")

print("-------------Invoking function with default arguments----------------")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file
print("------------------Invoking function with mix of default arguments----------")
introduction_with_mix_of_default_args("John")

# function that returns value(s)
print("-----------------------------function that returns value(s)------------------------------")
print("Product of two nos:")
print(product_of_two_num(4, 5))

# function with arbitrary arguments
print("---------------------function with arbitrary arguments----------------------------")
print("Result : ")
print(add_all_nums(5))

# Equivalant function
print("---------------------Equivalant function----------------------------")
print("Result : ")
print(double(5))

# Recursive function
print("---------------------Recursive function----------------------------")
print("Result of Fibonacci number : ")
print(fib(5))

# function level scoping
print("---------------------function level scoping----------------------------")
print("Subtraction of 2 nos :")
print(subtract(100, 40))

print("---------------------------palindrome string----------------------------------")
print(palindrome())

# print("------------------------ Another way of Palindrome string---- ---------------------\n")
# print(isPalindrome("bob"))


