def binary_search_position(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:

        mid = (left + right) // 2
        if target < numbers[mid]:
            right = mid - 1
        elif target > numbers[mid]:
            left = mid + 1
        else:
            return mid
    
    mid = "not found" #replace none
    return mid

print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
