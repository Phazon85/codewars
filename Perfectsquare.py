'''
Codewars Practice Problem
Write a function that takes an array of strings as an argument 
and returns a sorted array containing the same strings, 
ordered from shortest to longest.
'''
def sort_by_length(arr):
    return sorted(arr, key = len)
    

test = ["beg", "life", "i", "to"]

print(sort_by_length(test))