# Debugging During Development With assert
# Before moving on to the most common way of working with exceptions in Python using the try … except block, you’ll take a quick look at an exception that’s a bit different than the others.

# Python offers a specific exception type that you should only use when debugging your program during development. This exception is the AssertionError. The AssertionError is special because you shouldn’t ever raise it yourself using raise.

# Instead, you use the assert keyword to check whether a condition is met and let Python raise the AssertionError if the condition isn’t met.

# The idea of an assertion is that your program should only attempt to run if certain conditions are in place. If Python checks your assertion and finds that the condition is True, then that is excellent! The program can continue. If the condition turns out to be False, then your program raises an AssertionError exception and stops right away:


# Revisit my tiny script, exception.py, line 6-10

# Assuming that you’ll handle this constraint safely for your production system, you could replace this conditional statement with an assertion for a quick way to retain this sanity check during development:

number = 1
assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)

# If the number in your program is below 5, then the assertion passes and your script continues with the next line of code. However, if you set number to a value higher than 5—for example, 10—then the outcome of the assertion will be False:

number = 10
assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)

# -------------- error --------------
# Traceback (most recent call last):
#   File "Pyhton\TypeCasting__ErrorHandling\assertion.py", line 22, in <module>
#     assert (number < 5), f"The number should not exceed 5. ({number=})"
#             ^^^^^^^^^^
# AssertionError: The number should not exceed 5. (number=10)



# In this example, raising an AssertionError exception is the last thing that the program will do. The program will then come to halt and won’t continue. The call to print() that follows the assertion won’t execute.

# Using assertions in this way can be helpful when you’re debugging your program during development because it can be quite a fast and straightforward to add assertions into your code.

# However, you shouldn’t rely on assertions for catching crucial run conditions of your program in production. That’s because Python globally disables assertions when you run it in optimized mode using the -O and -OO command line options:



# In this run of your program, you used the -O command line option, which removes all assert statements. Therefore, your script ran all the way to the end and displayed a number that is dreadfully high!

# In production, your Python code may run using this optimized mode, which means that assertions aren’t a reliable way to handle runtime errors in production code. They can be quick and useful helpers when your debugging your code, but you should never use assertions to set crucial constraints for your program.

# If low.py should reliably fail when number is above 5, then it’s best to stick with raising an exception. However, sometimes you might not want your program to fail when it encounters an exception, so how should you handle those situations?

