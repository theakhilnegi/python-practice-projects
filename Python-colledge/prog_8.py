# linear search program
def linear_search(l,num):
    for i in range(len(l)):
        if(l[i]==num):
            return i
    return -1

list1=[12,87,45,23,44]
print("Element found at:",linear_search(list1,23))
