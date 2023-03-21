def list_max(l):
    max_num = l[0]
    for i in l:
    	if i > max_num:
            max_num = i
    return max_num

def list_min(l):
    min_num = l[0]
    for i in l:
    	if i < min_num:
            min_num = i
    return min_num

def list_sum(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum

list1 = []
num=int(input("Enter total items: "))
for i in range(num):
    print("Enter", i, "th item: ")
    x=int(input())
    list1.append(x)

# print("Enter the number in sequience: ")
# list1 = list(map(int, input().split()))

print("Maximum number is:", list_max(list1))
print("Minimum number is:", list_min(list1))
print("Sum of all number is:", list_sum(list1))





