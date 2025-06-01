# import sys

# input = sys.stdin.readline

# t,w=map(int,input().split())
# arr = [0] + [int(input()) for _ in range(t)]


# dp=[[0] * (w+1) for _ in range(t+1)]
# dp[1][0],dp[1][1] = arr[1]%2, arr[1]//2

# for t in range(2,t+1):
#     for w in range(w+1):

#         if w % 2 == 0:
#             j = arr[t] % 2 
#         else:
#             j = arr[t] // 2

#         dp[t][w] = max(dp[t-1][0:w+1]) + j

# print(max(dp[-1]))


# t초동안 최대 w번 움직여서 받을 수 있는 자두 개수. 1번에서 시작

t,w=map(int,input().split())
arr=[0]
for _ in range(t):
    arr.append((int(input().strip())))

dp=[[0]*(w+1) for _ in range(t+1)]


# 자두 이동횟수가 홀수(1번)이고 2번 나무에 떨어지면
# dp[i][j] = max(i-1초 일 때, j열의 자두수, i-1초 일 때 j-1열의 자두수) + 1
# 자두 이동횟수가 짝수(2번)이고 1번 나무에 떨어지면 
# dp[i][j] = max(i-1초 일 때, j열의 자두수, i-1초 일 때 j-1열의 자두수) + 1

for i in range(1,t+1):
    if arr[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1,w+1):
        if arr[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + 1
        elif arr[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[-1]))