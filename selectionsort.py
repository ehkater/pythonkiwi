def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1 )

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a

def read():
    #read from file
    f = open("data.csv","r")
    data = f.read().split()# convert string to list by split
    f.close()
    # for each element in list convert to int
    for i in range(len(data)):
        data[i] = str(data[i])
    return data