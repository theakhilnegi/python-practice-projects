file_1=open("file_4.txt")

test_list=file_1.readlines()
test_list = list(map(int, test_list))

print("Maximum number is: "+str(max(test_list)))
print("Minimum number is: "+str(min(test_list)))

file_1.close()