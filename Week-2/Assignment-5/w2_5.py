import bisect

def binary_search_first(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:

        mid = (left + right) // 2
        if target <= numbers[mid]: #change < to <=
            right = mid - 1
        elif target > numbers[mid]:
            left = mid + 1
        # else:
        #     return mid
    return left # target the leftmost value, which can assure returning the smallest value >= target 


print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2)) # should print 1 
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5)) # should print 2 
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3)) # should print 2
print(bisect.bisect_left([1, 2, 5, 5, 5, 6, 7], 2))
print(bisect.bisect_left([1, 2, 5, 5, 5, 6, 7], 5))
print(bisect.bisect_left([1, 2, 5, 5, 5, 6, 7], 3))

