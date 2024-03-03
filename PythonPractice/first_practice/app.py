# print("Hello, World!")
# ! Built in print function, string "Hello, World!"
# numList = [1,2,3,4,5,6]
# print(numList)
# ! Making an array, and printing it with built in function
# for x in numList:
#     print(x)
# !  Printing single indexes of array with for loop
# for x in numList:
#     print(x)
#     if x == 4:
#         break
# ! Print numList and stop @4
# name = input("What is your name? ")
# print("Hello " + name)
# ! Asks the user to enter their name, and then prints hello statement
# birth_year = input("enter your birth year ")
# age = 2024 - int(birth_year)
# print("your age is ", age)
# ! Asks you to enter your birth year, and then calculates what your age is and returns it

# int()
# float()
# bool()
# str()
# ! These are the functions to return something as a specific type (type conversion)
# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum: " +  str(sum))
# ! Has a user input two numbers, and returns the sum

# course = "python for beginners"
# print(course.capitalize())
# ! Prints course string with the first letter capitalized
# print(course.find('b'))
# ! Returns index of y in the string
# print(course.count('n'))
# ! Counts the number of Ns in the string 
# print(course.isspace())
# ! Tells you if the string is just blank space (has to have at least one space)
# blank_space = ' '
# print(blank_space.isspace())
# ! Returns True for isspace
# if 5 > 2:
#     print("Five is greater than two")
# first_number = int(input("Enter a number: "))
# second_number = int(input("Enter another number: "))
# if first_number > second_number:
#     print(first_number, "is greater than", second_number)
# if first_number < second_number:
#     print(first_number, "is less than", second_number)

"""
This is a 
Multiline
String.
These can be used for multiline
comments since they will be ignored unless
they are assigned to a variable
"""
# ! If you want to declare the type of a variable, use type  casting
# x = int(3)
# y = str(4)
# z = float(5)
# r = bool(1)
# print (x, y, z, r)
# print(type(y))
# ! Type returns the type of a variable that you enter into it
# ! Variable names can start with a letter or _, but they cannot start with a number
"""
camelCase
PascalCase
snake_case
"""
# a, b, c, d = "why", "does", "this", "work"
# print(a)
# print(b)
# print(c)
# print(d)
# ! You can assign multiple values to multiple variables in one line
# e = f = g = "cheese"
# print (e)
# print(f)
# print(g)
# ! Or you can have multiple variables assigned to the same value in one line
# fruits = ["apples", "bananas", "cherries"]
# h,i,j = fruits
# print(h)
# print(i)
# print(j)
# ! If you have an array, you can assign each index to a variable and print those variables seperately
# ! "Unpacking a collection"

# user_name = "Stevie"

# def returnName():
#     print("Welcome", user_name)
# returnName()
# ! def is the syntax to make a function in python

# def newFunc():
#     global gloVar
#     gloVar = "What are we talking about fellas?"
# newFunc()
# print("I wonder...", gloVar)
# ! you can make a global variable from a function by usinge the keyword global.
# ! The function must be called to use this global variable

# globalVariable = "cool"

# def changeGlobal():
#     global globalVariable
#     globalVariable = "radical"
# changeGlobal()
# print("Python is " + globalVariable)
# ! You can also use the keyword global inside a function to change a global variable
# ! outside of the function
# print(10>9)
# print(10==9)
# print(10<9)
# print(bool('hello'))
# number = 15
# print(bool(number))

# x = 200
# print(isinstance(x,int))
# print(isinstance(0,bool))
# print(5 ** 3)
# print(6 // 3)
# ! isinstance returns true or false depending on the type you input into it, and the variable you put into it
# thisList = {'apple', 'banana', 'cherry', 'orange'}
thisList = list(('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango'))
# ! Lists can either be made with curly brackets, or the list type and 2 sets of parenthesese
# print(thisList)
# print(len(thisList))
# ! len() returns the length of an object(not index!!!)
# print(thisList[1])
# ! By using [] you can access the index of a list
# print(thisList[-1])
# ! By using negative numbers you can access indexes of a list starting from the end
# print(thisList[3:6])
# ! You can access a range of indexes in a list
# ! If you leave out the first or second number, it will either start out from the beginning, or go until the end
thisList[3:6] = ["rutabega"]
# print(thisList)
# ! You can replace individual items in a list, or a range of items. Just make sure to containt the item or items
# ! That you are inserting with square brackets
thisList.insert(4, 'squirrel')
# print(thisList)
# ! You can use insert to insert an item into a list without replacing any other items
thisList.append('bangkok')
# ! append() adds an item to the end of the list
anotherList = ['creole', 'french', 'japanese', 'mandarin']
thisList.extend(anotherList)
# print(thisList)
# ! You can add one list to the end of another by using the extend method
# thisList.remove('squirrel')
# print(thisList)
# ! Remove deletes an item from a list, but you need to name the item itself, not it's index
# thisList.pop(2)
# print('deleting second index of thisList', thisList)
# ! pop deletes an item from a list by index
# ! If no index is specified, pop removes the last item
# del thisList[0]
# print('deleting first index of thisList', thisList)
# ! del also removes an item from a list by index
# thisList.clear()
# print('now clearing thisList', thisList)
# ! Clear completely empties a list
# for x in thisList:
#     print(x)
# ! Print all items in a list
# for i in range(len(thisList)):
#     print(thisList[i])
# ! Print all items by referring to their index numbers 
# *
# ?
# i = 0
# while i < len(thisList):
#     print(thisList[i])
#     i += 1
# ! While loops can also loop through lists
[print(x) for x in thisList]
# ? Shorthand for doing for loops
newList = [x for x in thisList if 'a' in x]
# print(newList)
# ? With one line of code you can create new lists from previous lists without looping
# ? List Comprehension
# * newlist = [expression for item in iterable if condition == True]
