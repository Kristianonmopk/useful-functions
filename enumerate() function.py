#The enumerate function takes in a list of values eg.a list or a tuple, and adds a counter as the key of the items in this list
#eg.
def capital_indexes(string):
  list1 = []
  for index, i in enumerate(string):
      if i.isupper():
          list1.append(index)
  return list1

