# sys module use 
import sys

n = len(sys.argv)
print("number of Arguments:", n)

	
Sum = 0
for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\nTotal Sum of Arguments:", Sum)
l=sys.argv
del l[0]
print("\nMaxmum of Arguments:",max(l))
print("\nMinimum of Arguments:",min(l))