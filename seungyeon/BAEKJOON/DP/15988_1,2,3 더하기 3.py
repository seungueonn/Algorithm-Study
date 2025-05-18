# n을 1,2,3의 합으로 나타내는 방법의 수 
# 1,2,3으로 n을 나타내는 방법 = dp -> dp[n]

import sys
input=sys.stdin.readline

dp=[0,1,2,4]


n=int(input().strip())
for _ in range(n):
    k=int(input().strip())
    for i in range(len(dp),k+1):
        dp.append((dp[i-1] + dp[i-2] + dp[i-3] ) %1000000009)

    print(dp[k])
