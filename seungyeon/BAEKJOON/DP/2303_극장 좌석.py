import sys
input=sys.stdin.readline

n=int(input().strip())
m=int(input().strip())

vip=[]
for i in range(m):
    vip.append(int(input().strip()))

dp=[1] * 45
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

if n < 2:
    print(1)
else:
    answer=1
    srt=1

    for j in vip:
        answer *= dp[j-srt]
        srt = j + 1

    print(answer * dp[n+1-srt])
