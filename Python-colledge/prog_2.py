# 3x4 matrix multiplication
x = [[11,22,33],
    [44,55,66],
    [77,88,99]]
y = [[1,2,3,4],
    [5,6,7,8],
    [9,1,2,3]]

ans = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(x)):
   for j in range(len(y[0])):
       for k in range(len(y)):
           ans[i][j] += x[i][k] * y[k][j]

for c in ans:
   print(c)