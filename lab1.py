l = [1, 2, 3, 8, 4, 5, 6]

"""finds the max of a list of numbers and returns the value (not the index)
If int_list is empty, returns None. If list is None, raises ValueError"""


def max_list_iter(int_list):  # must use iteration not recursion
    if int_list is None:
        raise ValueError
    if type(int_list) != list:
        raise ValueError
    for item in int_list:
        if type(item) != int:
            raise ValueError
    if len(int_list) == 0:
        return None
    else:
        max = int_list[0]
    for i in range(len(int_list)):
        if max < int_list[i]:
            max = int_list[i]
    return max


"""recursively reverses a list of numbers and returns the reversed list
If list is None, raises ValueError"""
newList = []


def reverse_rec(int_list):  # must use recursion
    global newList
    if int_list == None:
        raise ValueError
    if type(int_list) != list:
        raise ValueError
    for item in int_list:
        if type(item) != int:
            raise ValueError
    if int_list == []:
        int_list = newList
        newList = []
        return int_list
    else:
        newList.append(int_list.pop())
        return (reverse_rec(int_list))


"""searches for target in int_list[low..high] and returns index if found
If target is not found returns None. If list is None, raises ValueError """


def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if type(int_list) != list:
        raise ValueError
    for item in int_list:
        if type(item) != int:
            raise ValueError
    int_list.sort()
    check = int_list[(low + high) // 2]
    idx = int_list.index(check)
    if check == target:
        return idx
    elif check > target and idx==0:
        return None
    elif check < target:
        if int_list[idx + 1] == target:
            return idx+1
        elif idx+1 == len(int_list)-1:
            return None
        return bin_search(target, idx, high, int_list)
    elif check > target:
        return bin_search(target, low, idx, int_list)



