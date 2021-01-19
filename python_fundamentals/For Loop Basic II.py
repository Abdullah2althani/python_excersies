# 1. Biggie Size - Given a list,
# write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) 
# returns that same list, but whose values are now[-1, "big", "big", -5]

# def biggie_size(m):
    
#     for i in range(len(m)):
#             if m[i] > 0:
#                 m[i] = "big"
#     return m

# arr = [-1, 3, 5, -5]
# print(biggie_size(arr))


# 2.Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1, 1, 1, 1]) changes the original list to[-1, 1, 1, 3] and returns it
# Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list to[1, 6, -4, -2, -7, 2] and returns it

# counter = 0
# def count_positives(pp):
#     for i in range(len(pp)):
#         if pp[i] > 0:
#             counter += 1
#     last_i = len(pp) - 1
#     pp[last_i] = counter
#     return pp
    
# print(count_positives([1, 6, -4, -2, -7, -2]))

#  3.Sum Total - Create a function that takes a list and 
#    returns the sum of all the values in the list.
#    Example: sum_total([1, 2, 3, 4]) should return 10
#    Example: sum_total([6, 3, -2]) should return 7

# def sum_total(a):
#     sum = 0 
#     for i in range (len(a)):
#         sum += a[i]
#     return sum

# arr = [1, 2, 3, 4]
# print(sum_total(arr))

#  4.Average - Create a function that takes a list and returns the average of all the values.x
#    Example: average([1, 2, 3, 4]) should return 2.5

# def average(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
    
#     length = len(arr)
#     avg = sum / length

#     return avg

# m = [1, 2, 3, 4]
# print(average(m))

#  5.Length - Create a function that takes a list and returns the length of the list.
#    Example: length([37, 2, 1, -9]) should return 4
#    Example: length([]) should return 0

# def length(q):
#     return len(q)
# print(length([37, 2, 1, -9]))

#  6.Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#    Example: minimum([37, 2, 1, -9]) should return -9
#    Example: minimum([]) should return False

# def minimum(w):
#     min = w[0]
#     for i in range(1,len(w),1):
#         if(w[i]< min):
#             min = w[i]
#     return min

# print(minimum([37, 2, 1, -9]))

#  7.Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#    Example: maximum([37, 2, 1, -9]) should return 37
#    Example: maximum([]) should return False

# def maximum(w):
#     max = w[0]
#     for i in range(1,len(w),1):
#         if(w[i]> max):
#             max = w[i]
#     return max

# print(maximum([37, 2, 1, -9]))

#  8.Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#    Example: ultimate_analysis([37, 2, 1, -9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}

# def ultimate_analysis(z):
#     sum = 0
#     min = z[0]
#     max = z[0]
#     for i in range(len(z)):
#         sum += z[i]
#         if(z[i]< min):
#             min = z[i]
#         if(z[i]> max):
#             max = z[i]
            
#     length = len(z)
#     avg = sum / length
    
#     analysis = {
#         'sumTotal': sum,
#         'average': avg,
#         'minimum': min,
#         'maximum': max,
#         'length': length
#     }

#     return analysis

# print(ultimate_analysis([37, 2, 1, -9]))  
  
#  9.Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#    Example: reverse_list([37, 2, 1, -9]) should return [-9, 1, 2, 37]
# def reverse_list(r):
#     n = 0
#     newr = []
#     for i in range(len(r), 0, -1):          
#         newr[n] = r[i]
#         n = n + 1 
#     return newr
# print (reverse_list([37, 2, 1, -9]))