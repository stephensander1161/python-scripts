
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1: 
        return sequence
    else: 
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence: 
        if item > pivot:
            items_greater.append(item)

        else: 
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([43323,543457,6,5,4,888,7798,54674,3353453]))