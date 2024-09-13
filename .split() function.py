#The split() method splits a string into a list.
#You can specify the separator, default separator is any whitespace.
""""
Parameter	  Description
separator	  Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	  Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
"""
#Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

#When no separator or maxsplit parameter is given, the split() method will split the string from every whitespace.
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split()
print(x)

#When a separator paremeter is given but no maxsplit parameter is given, the split() method will split the string from the specified separator each time it appearfs in the string.
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

#When both parameters are given, the split() method will split the string from the specified separator for the specified number of times.
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)
