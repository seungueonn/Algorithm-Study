# dp[n][0] = R 일때
# dp[n][1] = G 일때
# dp[n][2] = B 일때

import sys
input=sys.stdin.readline

n = int(input())
arr=[]
dp= [0]*n
for i in range(n):
    dp[i] = list(map(int,input().split()))

for i in range(1,n): # 1부터 시작, 0일 때의 최소값은 알아서 가져옴
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + dp[i][0] # R을 색칠 할 때, 전에 색칠한 것중에(G,B) 최소값 가져오기
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + dp[i][2]

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))

