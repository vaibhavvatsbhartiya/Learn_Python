# Raising an Exception in Python
# There are scenarios where you might want to stop your program by raising an exception if a condition occurs. You can do this with the raise keyword:

# You can even complement the statement with a custom message. Assume that you’re writing a tiny toy program that expects only numbers up to 5. You can raise an error when an unwanted condition occurs:

number = 10
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)

# In this example, you raised an Exception object and passed it an informative custom message. You built the message using an f-string and a self-documenting expression.

# When you run low.py, you’ll get the following output:

# Traceback (most recent call last):
#   File "./exception.py" 
#     raise Exception(f"The number should not exceed 5. ({number=})")
# Exception: The number should not exceed 5. (number=10)




# The program comes to a halt and displays the exception to your terminal or REPL, offering you helpful clues about what went wrong. Note that the final call to print() never executed, because Python raised the exception before it got to that line of code.

# With the raise keyword, you can raise any exception object in Python and stop your program when an unwanted condition occurs.