def bin_search(array, item):
    low = 0
    high = len(array)
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return guess
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None


my_array = [1, 5, 7, 10, 22]
bin_search(my_array, 7)
