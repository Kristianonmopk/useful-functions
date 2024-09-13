#The .replace function in python allows you to replace a letter/character in string with another character. 
#Below is an example of the .replace function being used in a function to replace all instances of a '.' in a string with '', essentially just removing all occurences of the '.' character.

def remove_dots(string):
  string = string.replace('.', '')
  return string

#Alternatively however, we can alos use the .replace function to replace/get rid of a certain letter in a string.
#For example, in the example below, we use the .replace function to replace the first 's' character in the string with the character 't' however, this does not affect the other 's' characters in the string.
def replace_s(string):
  string = string.replace('s', 't', 1)
  return string
