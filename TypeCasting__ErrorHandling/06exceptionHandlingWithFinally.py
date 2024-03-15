# Cleaning Up After Execution With finally
# Imagine that you always had to implement some sort of action to clean up after executing your code. Python enables you to do so using the finally clause:

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")


# ...01 <code>

# try:
#     linux_interaction()
# except RuntimeError as error:
#     print(error)
# else:
#     try:
#         with open("file.log") as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print("Cleaning up, irrespective of any exceptions.")

# ...........  </code>
    
# In this code, Python will execute everything in the finally clause. It doesn’t matter if you encounter an exception somewhere in any of the try … except blocks. Running the code on a macOS or Windows machine will output the following:


#  -------------------output-------------------
# python -u "TypeCasting__ErrorHandling\06exceptionHandlingWithFinally.py"
# Function can only run on Linux systems.
# Cleaning up, irrespective of any exceptions.


# Note that the code inside the finally block will execute regardless of whether or not you’re handling the exceptions:

# ...02 <code>

try:
    linux_interaction()
finally:
    print("Cleaning up, irrespective of any exceptions.")

# ...........  </code>
    
# You simplified the example code from above, but linux_interaction() still raises an exception on a macOS or Windows system. If you now run this code on an operating system other than Linux, then you’ll get the following output:
    

#  -------------------output-------------------
# Cleaning up, irrespective of any exceptions.
# Traceback (most recent call last):
#   ...
# RuntimeError: Function can only run on Linux systems.



# Despite the fact that Python raised the RuntimeError, the code in the finally clause still executed and printed the message to your console.

# This can be helpful because even code outside of a try… except block won’t necessarily execute if your script encounters an unhandled exception. In that case, your program will terminate and the code after the try … except block will never run. However, Python will still execute the code inside of the finally clause. This helps you make sure that resources like file handles and database connections are cleaned up properly.