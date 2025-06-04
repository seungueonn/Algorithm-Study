# import sys
# input=sys.stdin.readline

# n = int(input())

# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split(" "))))

# dp=[0 for i in range(n+1)]

# for i in range(n-1,-1,-1):
#     if i + arr[i][0] > n:
#         dp[i] = dp[i+1]
#     else :
#         dp[i] = max(dp[i+1],arr[i][1] + dp[i+arr[i][0]]) 
# print(dp[0])


# 상담을 해서 얻을 수 있는 최대 이익


import sys
input=sys.stdin.readline

n=int(input().strip())

dp = [0] * (n+1)
for i in range(1,n+1):
    t,p =map(int,input().split())

    dp[i] = max(dp[i-1],dp[i])

    if i + t <= n+1:
        dp[i+t-1] = max(dp[i-1]+p,dp[i+t-1])

print(dp[-1])
