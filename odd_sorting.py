'''
codewars.com practice problem
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
'''

def sort_array(source_array):
    temp = sorted([i for i in source_array if i%2 != 0])
    odd_int = 0
    if source_array == []:
        return source_array
    else:
        for i in range(len(source_array)):
            if source_array[i] % 2 != 0:
                source_array[i] = temp[odd_int]
                odd_int += 1
        return source_array




test = [5, 3, 2, 8, 1, 4]


print(sort_array(test))