#Adding a comment in Repo
# Type Conversion --> to changhe the data type of a variable#
# Convert Floats and Numeric strings to int
'''
print(int("20"))
print(type(int("20")))

print(float("14.21"))
#print(type(float("14.21")))#Errors out because int expects only whole numbers inside quotes

print(int(float("20.24")))

##Strings##
#3 ways to create a string- using either single, double,or triple quotes
first_name = "Jane"
last_name = 'Doe'
address =''10 Main Street''


job = "Physician's Assistant"

#3String function##
# len() --> returns number of charaters in the string
print(len("Hello"))

# upeer and lower --> Convert string to appropriate case

print("Hello".upper())

# String concatenation- adding up strings
first_name = "Jane"
last_name = "Doe"
age = 24

print(first_name + " " + last_name + ": " + str(age))

#SWtring multiplication - can multiple a string with an int
print("hello "*3)

# Accessing string characters - a string is just ba sequence of characters
'''

name = "Jane Doe"
print(name[2])

#print(name[8])# throws index out of bound error

# Retrieving the character at a giver index
print (name.index('o'))







