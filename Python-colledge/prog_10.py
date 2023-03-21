# selection sort 

# void selection_sort(int arr[], int size){
#     int min;
#     for (int i = 0; i < size-1; i++)
#     {
#         min=i;       //a[min] is supposed to be smallest
#         for (int j = i; j < size-1; j++)
#         {
#             if(arr[min]>arr[j+1]){
#                 min=j+1;
#             }
#         }        
#         swap(&arr[i],&arr[min]);
#     }
# }

def selection_sort(l):
    min=0
    for i in range(len(l)-1):
        min=i
        for j in range(i,len(l)-1):
            if(l[min]>l[j+1]):
                min=j+1
        l[i],l[min]=l[min],l[i]


print("Enter the number in sequience: ")
list1 = list(map(int, input().split()))
print("Unsorted array:",list1)
selection_sort(list1)
print("Sorted array:",list1)

