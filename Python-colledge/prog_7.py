# greatest number in list
def list_max(l):
    max = l[0]
    for i in l:
    	if i > max:
            max = i
    return max

list1 = [33,56,12,39,63]
print("Greatest number is:", list_max(list1))

