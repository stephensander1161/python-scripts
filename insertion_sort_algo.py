def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length: 
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a

print(insertion_sort([4,3,3,3,543345,2342344565,23423424547567565,324256543,23423423424,87,77,66546456988756,343,2234,2,35,2]))