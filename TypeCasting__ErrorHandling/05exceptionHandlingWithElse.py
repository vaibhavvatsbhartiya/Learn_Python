# Proceeding After a Successful Try With else
# You can use Python’s else statement to instruct a program to execute a certain block of code only in the absence of exceptions:

# example

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
#     print("Doing even more Linux things.")

# ...........  </code>



# If you were to run this code on a Linux system, then the output would be the following:

# -------------------output-------------------
# $ python linux_interaction.py
# Doing Linux things.
# Doing even more Linux things.
    


# Because the program didn’t run into any exceptions, Python executed the code in the else clause. However, if you run this code on a macOS or Windows system, then you get a different output:
    
# -------------------output-------------------
# $ python linux_interaction.py
# Function can only run on Linux systems.
    


# The linux_interaction() function raised a RuntimeError. You’ve handled the exception, so your program doesn’t crash, and instead prints the exception message to the console. The code nested under the else clause, however, doesn’t execute, because Python encountered an exception during execution.

# Note that structuring your code like this is different from just adding the call to print() outside of the context of the try … except block:


# Nesting code under the else clause assures that it’ll only run when Python doesn’t encounter any exception when executing the try … except block.

# You can also create a nested try … except block inside the else clause and catch possible exceptions there as well:

# ...02 <code>

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

# ...........  </code>
        
# If you were to execute this code on a Linux machine, then you’d get the following result:

#  -------------------output-------------------
# $ python 
# Doing Linux things.
# [Errno 2] No such file or directory: 'file.log'


# From the output, you can see that linux_interaction() ran. Because Python encountered no exceptions, it attempted to open file.log. That file didn’t exist, but instead of letting the program crash, you caught the FileNotFoundError exception and printed a message to the console.