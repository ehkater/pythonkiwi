import time

start_time = time.time()

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

def write(thelist):
    #create edit the text file
    file = open("data.csv", "wt")
    # for each element in list write i value and add space between new value
    for i in range(len(thelist)):
        file.write(str(thelist[i]) + " ")
    file.close()
    
thelist = read()
print(bubblesort(thelist))
write(thelist)

end_time = time.time()

print(end_time - start_time)