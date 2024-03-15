# In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.

# There are two types of type conversion in Python.

# 1. Implicit Conversion - automatic type conversion
# 2. Explicit Conversion - manual type conversion




# Implicit Conversion:
# In certain situations, Python automatically converts one data type to another. 
# This is known as implicit type conversion.

ab = 24
cd = 2.4


# Explicit Type Conversion:
# In Explicit Type Conversion, users convert the data type of an object to required data type.

# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.

# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))






# Key Points to Remember
# 1. Type Conversion is the conversion of an object from one data type to another data type.
# 2. Implicit Type Conversion is automatically performed by the Python interpreter.
# 3. Python avoids the loss of data in Implicit Type Conversion.
# 4. Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
# 5. In Type Casting, loss of data may occur as we enforce the object to a specific data type.
