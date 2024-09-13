#The special syntax * in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 
#The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.

#For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together. It can be done using *args.
#Eg.
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

input()

#Python program to illustrate *args for a variable number of arguments
def myFun2(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun2('Hello', 'Welcome', 'to', 1234)

input()

#The special syntax ** in function definitions in Python is used to pass a keyworded, variable-length argument list. We use the symbol ** to take in a variable number of keyword arguments; by convention, it is often used with the name kwargs.
#A keyword argument is where you provide a name to the variable as you pass it into the function.
#One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

#Python program to illustrate *kwargs for a variable number of keyword arguments. Here **kwargs accept keyworded variable-length argument passed by the function call. for first=’Geeks’ first is key and ‘Geeks’ is a value. in simple words, what we assign is value, and to whom we assign is key. 
def myFun3(**kwargs):
  for key, value in kwargs.items():
      print(key, value)

myFun3(first='Geeks', mid='for', last='Peeps')

input()

#Here, we are passing *args and **kwargs as an argument in the myFun function. where ‘geeks’, ‘for’, ‘geeks’ is passed as *args, and first=”Geeks”, mid=”for”, last=”Geeks”  is passed as **kwargs and printing in the same line.
def myFun4(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun4('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
