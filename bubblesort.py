def bubblesort(mylist):
    for i in range (0, len(mylist) - 1): 
        for j in range (0 , len(mylist) - 1 - i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist

def read():
    #read from file
    f = open("data.csv","r")
    data = f.read().split()# convert string to list by split
    f.close()
    # for each element in list convert to int
    for i in range(len(data)):
        data[i] = str(data[i])
    return data