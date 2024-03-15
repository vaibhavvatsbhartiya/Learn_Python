print('hello v2')
# hello v2 : string

# Variables

num = 20 # number
num2 = 20.02 # float
num3= True # boolean

# now let's see how to take input in python
name = input('enter your name ') 
print('hello ' +  name) # this is called string concatenation as i am adding two different strings with each other

# type conversion
birth_year = int(input('enter your bitrh year: '))
age = 2024 - birth_year
print(age)

# there are 4 types of functions available for typer conversion
int()
bool()
float()
str()

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)