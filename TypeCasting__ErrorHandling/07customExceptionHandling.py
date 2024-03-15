# Creating Custom Exceptions in Python
# With the large number of built-in exceptions that Python offers, you’ll likely find a fitting type when deciding which exception to raise. However, sometimes your code won’t fit the mold.

# Python makes it straightforward to create custom exception types by inheriting from a built-in exception. Think back to your linux_interaction() function:

# ...01 <code>

# def linux_interaction():
#     import sys
#     if "linux" not in sys.platform:
#         raise RuntimeError("Function can only run on Linux systems.")
#     print("Doing Linux things.")

# ..... </code>



# Using a RuntimeError isn’t a bad choice in this situation, but it would be nice if your exception name was a bit more specific. For this, you can create a custom exception:

class PlatformException(Exception):
    """Incompatible platform."""

# You generally create a custom exception in Python by inheriting from Exception, which is the base class for most built-in Python exceptions as well. You could also inherit from a different exception, but choosing Exception is usually the best choice.

# That’s really all that you need to do. In the code snippet above, you also added a docstring that describes the exception type and serves as the class body.

# Note: Python requires some indented code in the body of your class. Alternatively to using the docstring, you could’ve also used pass or the ellipsis (...). However, adding a descriptive docstring adds the most value to your custom exception.

# While you can customize your exception object, you don’t need to do that. It’s often enough to give your custom Python exceptions a descriptive name, so you’ll know what happened when Python raises this exception in your code.

# Now that you’ve defined the custom exception, you can raise it like any other Python exception:

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise PlatformException("Function can only run on Linux systems.")
    print("Doing Linux things.")


try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    print("Doing even more Linux things.")


# You could even use your custom PlatformException as a parent class for other custom exceptions that you could descriptively name for each of the platforms that users may run your code on.
    
#  -------------------output-------------------
#  python -u "Roadmap\Pyhton\TypeCasting__ErrorHandling\07customExceptionHandling.py"
# Traceback (most recent call last):
#   File "Pyhton\TypeCasting__ErrorHandling\07customExceptionHandling.py", line 41, in <module>
#     linux_interaction()
#   File "TypeCasting__ErrorHandling\07customExceptionHandling.py", line 36, in linux_interaction
#     raise PlatformException("Function can only run on Linux systems.")
# PlatformException: Function can only run on Linux systems.