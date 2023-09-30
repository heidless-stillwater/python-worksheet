
# extend vs append
# Python’s append() method is used to add elements to the existing list.fruits = ["apple","banana","grapes"]
print('')
#initialization of list
fruits = ["apple","banana","grapes"]

#print before appending
print("list of fruits before append -> " + str(fruits))

#appending entire list
fruits.append(["peach","mango","watermelon"])

#print after appending
print("list of fruits after append -> " + str(fruits))

# The extend() method acts the same as the append() method if we add a single element, but it behaves differently if we add a list.
#initialization of list
print('')
fruits = ["apple","banana","grapes"]

#print before extend
print("list of fruits before extend -> " + str(fruits))

#appending entire list
fruits.extend(["peach","mango","watermelon"])

#print after extend
print("list of fruits after extend -> " + str(fruits))

print('')