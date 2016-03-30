def binary_search(value, items, low, high):
    if low > high:
        return None
    middle = low + ((high- low) // 2)
    print('low', low, 'middle', middle, 'high', high)
    if items[middle] > value:
        return binary_search(value, items, low, middle-1)
    elif  items[middle] < value:
        return binary_search(value, items, middle + 1, high)
    else:
        return middle
items = range(1, 101)
index = binary_search(12, items, 1, 100)
print("Index is {}, value is {}".format(index, items[index]))
