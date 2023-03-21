data = open("file1.txt","r")
word = ""
freq = 0
dic = []
for line in data:
	line_word = line.lower().replace('.','').replace(',','').split(" ")
	for w in line_word:
		dic.append(w)		
for i in range(0, len(dic)):
	flag = 1
	for j in range(i+1, len(dic)):
		if(dic[i] == dic[j]):
			flag = flag + 1

	if(flag > freq):
		freq = flag
		word = dic[i]

print("Repeated word: " + word + " and it occur " + str(freq) + " times")
data.close()
