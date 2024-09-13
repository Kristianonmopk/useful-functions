#Python join() is an inbuilt string function used to join elements of a sequence separated by a string separator. This function joins elements of a sequence and makes it a string.
#Below is an example of the join() function being used in a function to recreate the given word with '.'s between each letter

def add_dots(string):
  string = '.'.join(string)
  return string

#We can also use the reverse method of the join() function to reverse the order of a word in python as shown in the code below

s = 'Python' #initial string
reversed=''.join(reversed(s)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string
