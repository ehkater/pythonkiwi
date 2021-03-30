import time
import matplotlib.pyplot as plt

start_time = time.time()


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

def write(list_a):
    #create edit the text file
    file = open("data.csv", "wt")
    # for each element in list write i value and add space between new value
    for i in range(len(list_a)):
        file.write(str(list_a[i]) + " ")
    file.close()

list_a = read()
print(selection_sort(list_a))
write(list_a)

end_time = time.time()

print(end_time - start_time)




plt.plot(list_a)

plt.title('kiwi weight distribution')
plt.show()