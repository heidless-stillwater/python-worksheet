my_list = ["Lesson", 5, "Is Fun?", True]
print(my_list)

print('')

second_list = list("Life is Study")  # Create a list from a string
print(second_list)

print('')

second_list.remove('f')
print(second_list)

print('')


third_list = list(range(1,16))
print(third_list)
third_list.remove(6)
print(third_list)

print('')

empty_list = []
print( empty_list )

empty_list.append("I'm no longer empty!")
print(empty_list)

combined_list = my_list + empty_list
print(combined_list)
['Lesson', 5, 'Is Fun?', True, "I'm no longer empty!"]

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
fruits = ["apple","banana","grapes"]

#print before extend
print("list of fruits before extend -> " + str(fruits))

#appending entire list
fruits.extend(["peach","mango","watermelon"])

#print after extend
print("list of fruits after extend -> " + str(fruits))

print('')

num_list = [1, 3, 5, 7, 9]
print( len(num_list))                # Check the length
print( max(num_list))                # Check the max
print( min(num_list))                # Check the min
print( sum(num_list))                # Check the sum
print( sum(num_list)/len(num_list))  # Check the mean*

print('')

### Other common list functions include list.sort() and list.reverse():
new_list = [1, 5, 4, 2, 3, 6]      # Make a new list

new_list.reverse()                 # Reverse the list
print("Reversed list", new_list)

new_list.sort()                    # Sort the list
print("Sorted list", new_list)

print('')

# slice
another_list = ["Hello","my", "bestest", "old", "friend."]
my_slice =  another_list[1:3]   # Slice index 1 and 2
print(my_slice )
['my', 'bestest']

# Slice the entire list but use step size 2 to get every other item: 
print(another_list)
my_slice =  another_list[0:6:2] 
print(my_slice )

print('')

