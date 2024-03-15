# In Python, you use the try and except block to catch and handle exceptions. Python executes code following the try statement as a normal part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause:

# try 
#     {}
# except
#     {}

# As you saw earlier, when syntactically correct code runs into an error, Python will raise an exception error. This exception error will crash the program if you don’t handle it. In the except clause, you can determine how your program should respond to exceptions.

# The following function can help you understand the try and except block:

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

# The linux_interaction() can only run on a Linux system. Python will raise a RuntimeError exception if you call it on an operating system other then Linux.

# You can give the function a try by adding the following code:
# ... 1 <code>

# try:
#     linux_interaction()
# except:
#     pass 

# ------------------------ </code>

# The way you handled the error here is by handing out a pass. If you run this code on a macOS or Windows machine, then you get the following output:  python -u "Pyhton\TypeCasting__ErrorHandling\04exceptionHandling.py"

# You got nothing in response. The good thing here is that your program didn’t crash. But letting an exception that occurred pass silently is bad practice. You should always at least know about and log if some type of exception occurred when you ran your code.

# To this end, you can change pass into something that generates an informative message:

# so 
# ... 2 <code>

# try:
#     linux_interaction()
# except:
#     print("Linux function wasn't executed.")

# ------------------------ </code>
    
# When you now execute this code on a macOS or Windows machine, you’ll see the message from your except block printed to the console: python -u "Pyhton\TypeCasting__ErrorHandling\04exceptionHandling.py"
# Linux function wasn't executed.



# When an exception occurs in a program that runs this function, then the program will continue as well as inform you about the fact that the function call wasn’t successful.

# What you didn’t get to see was the type of error that Python raised as a result of the function call. In order to see exactly what went wrong, you’d need to catch the error that the function raised.

# The following code is an example where you capture the RuntimeError and output that message to your screen:
# ... 3 <code>

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
    print("The linux_interaction() function wasn't executed.")

# ------------------------ </code>