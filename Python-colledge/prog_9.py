# binary search 

# int search(int arr[], int size, int item)
# {
#     int low = 0, mid, high = size - 1, flag = 1;
#     while (low <= high)
#     {
#         mid = (low + high) / 2;
#         if (arr[mid] == item)
#         {
#             printf("Item is found on %d place", mid + 1);
#             return 1;
#         }
#         if (item > arr[mid])
#         {
#             low = mid + 1;
#         }
#         else
#         {
#             high = mid - 1;
#         }
#     }
#     printf("Item not found!!!");
#     return 0;
# }


def binary_search(l,item):
    low=0
    mid=0
    high=len(l)-1
    flag=1
    while(low<=high):
        mid=(low+high)//2
        if(l[mid] == item):
            print("Item is found at place",mid+1)
            return 1

        if(item>l[mid]):
            low=mid+1

        else:
            high=mid+1
    
    print("Item not found")
    return 0

print("Enter the number in sequience: ")
list1 = list(map(int, input().split()))
num=int(input("Enter the number to be searched: "))
binary_search(list1,num)