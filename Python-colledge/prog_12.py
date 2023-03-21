def merge(arr1, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr1[l + i]

    for j in range(0 , n2):
    	R[j] = arr1[m + 1 + j]
    i = 0	 
    j = 0	 
    k = l	 

    while i < n1 and j < n2 :
    	
        if L[i] <= R[j]:
            arr1[k] = L[i]
            i =i+ 1
        else:
            arr1[k] = R[j]
            j =j+1
        k += 1

    while i < n1:
        arr1[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr1[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,l,r):
	
    if l < r:
        m = (l+(r-1))//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


arr = [9,77,56,1,3,44,5,67]
n = len(arr)
print ("Given array is")
for i in range(n):
    print (arr[i],end="   ")

mergeSort(arr,0,n-1)
print ("\n\n\nSorted array using merge sort is")
for i in range(n):
    print (arr[i],end="   ")
