def binary_search_recursive(list, search, first, last):
    if first > last:
        return f"{search} not found"
    middle = (first + last) // 2

    if list[middle] == search:
        return f'{search} found at position {middle}'
    elif search < list[middle]:
        return binary_search_recursive(list, search, first, middle - 1)
    else:
        return binary_search_recursive(list, search, middle + 1, last)

def binary_search(list, search):
    first = 0
    last = len(list) - 1
    middle = (first + last) // 2

    while list[middle] != search:
        if first > last:
            return f"{search} not found"
        if search < list[middle]:
            last = middle - 1
        else:
            first = middle + 1
        middle = (first + last) // 2

    return f'{search} found at position {middle}'

list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]

for i in list:
    search = i
    print(f'Binary search: {binary_search(list, search)}')
    print(f'Recursive binary search: {binary_search_recursive(list, search, 0, len(list)-1)}')