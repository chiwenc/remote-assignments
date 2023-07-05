def count(input):
    my_dic = {}

    for element in input:
        my_dic[element] = my_dic.get(element, 0 ) + 1
    
    return my_dic

def group_by_key(input):
    my_dic = {}
    key_list = [input[i]['key'] for i in range(len(input))]
    value_list = [input[i]['value'] for i in range(len(input))]
    my_list = list(zip(key_list, value_list)) # create list since dictionary cannot iterate over duplicate keys

    for i in range(len(my_list)):
        my_dic[my_list[i][0]] = my_dic.get(my_list[i][0],0) + my_list[i][1]
    return my_dic

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
]

print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}






