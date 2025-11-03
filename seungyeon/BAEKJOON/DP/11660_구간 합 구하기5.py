import sys
input=sys.stdin.readline

n,m=map(int,input().split())

dp=[[0] * (n+1) for _ in range(n+1)]

arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):

        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

for k in range(m):
    a,b,c,d=map(int,input().split())

    answer = dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1]

    print(answer)