# insertion sort 

# void insertion_sort(int arr[],int size){
#     int j;
#     int flag;
#     for (int i = 1; i <= size-1; i++)
#     {
#         flag=arr[i];
#         j=i-1;
#         while(flag<arr[j]&&j!=-1){
#             arr[j+1]=arr[j];
#             j--;
#         }
#         arr[j+1]=flag;
#     }
# }

def insertion_sort(l):
    j=0
    flag=0
    for i in range(1,len(l)):
        flag=l[i]
        j=i-1
        while(flag<l[j] and j!=-1):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=flag


print("Enter the number in sequience: ")
list1 = list(map(int, input().split()))
print("Unsorted array:",list1)
insertion_sort(list1)
print("Sorted array:",list1)
