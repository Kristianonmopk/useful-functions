#bool is a casting operator just like int and str and can be used to turn an integer or a string into a boolean value.

#For example, we have a variable called x, which is set to the integer 5. We then use the bool() function to turn it into a boolean value which is True.

x = 5 
print(bool(x))

#In this other example below, we have a variable called y, which is set to the string "Hello". We then use the bool() function to turn it into a boolean value which is True.

y = "Hello"
print(bool(y))

#Furthermore, in this example below, we have a variable called b, which is set to the string "0" We then use the bool() function to turn it into a boolean value which is True

b = "0"
print(bool(b))

#However, in this example below, we have a variable called z, which is set to the integer 0. We then use the bool() function to turn it into a boolean value which is False.

z = 0
print(bool(z))


#In this example below, we have a variable called a, which is set to none. We then use the bool() function to turn it into a boolean value which is false

a = None
print(bool(a))

"""Overall, the bool() function returns False: 
.If a False value is passed.If None is passed.
.If an empty sequence is passed, such as (), [], ”, etc.
.If Zero is passed in any numeric type, such as 0, 0.0, etc.
.If an empty mapping is passed, such as {}.
.If Objects of Classes having __bool__() or __len()__ method, returning 0 or False."""
