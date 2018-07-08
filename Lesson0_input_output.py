n = int(input())
cash = [1, 5, 10, 20, 50, 100]
rlt = [[1, 0, 0, 0, 0, 0] for i in range(n+1)]
for i in range(1, 6):
    for j in range(0, n+1):
        for k in range(0, j//cash[i] + 1):
            rlt[j][i] += rlt[j - k * cash[i]][i-1]
            
print(rlt[n][5])