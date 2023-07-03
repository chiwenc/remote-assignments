def find_max(numbers):
    max = numbers[0]

    for n in range(1, len(numbers)):
        if numbers[n] > max:
            max = numbers[n]
    return max

def find_position(numbers,target):
    position = 0
    
    if target not in numbers:
        position = -1 
    else:
        for n in range(len(numbers)):
            if target != numbers[n]:
                continue
            elif target == numbers[n]:
                position = n
                break
    return position


print(find_max([1, 2, 4, 5])) # should print 5
print(find_max([5, 2, 7, 1, 6])) # should print 7
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1
