def qsort(list):
    if len(list) < 2:
        return list
    pivot = list[0]
    less = [i for i in list[1:] if i <= pivot]
    greater = [i for i in list[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)


print(qsort([10, 5, 2, 3]))
