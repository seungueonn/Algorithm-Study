# import sys
# input=sys.stdin.readline

# n,m=map(int,input().split())

# arr=[]
# for i in range(n):
#     arr.append(int(input()))

# arr.sort()

# l,r=0,0
# answer=2000000000


# while(r < n): # right를 움직이는 이유는 더 큰 숫자에서 현재 값을 빼서 더 큰 차이를 갖기 위해서

#     if arr[r]-arr[l] > m:
#         answer = min(answer,arr[r]-arr[l])
#         l += 1
#     elif arr[r]-arr[l] < m:
#         r += 1
#     else :
#         answer = m
#         break

# print(answer)


# 수열에서 2개를 골랐을 때 차이가 m이상이면서 제일 작은 수 


import sys
input=sys.stdin.readline

n,m=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append((int(input().strip())))

arr.sort()

l,r=0,0

answer=2000000000

while r < n :

    if arr[r] - arr[l] > m: # 클 때 -> m이상중에 최소값
        answer=min(answer,arr[r]-arr[l])
        l += 1

    elif arr[r]-arr[l] < m:
        r += 1

    else: # m이면 끝 -> m이상중에 최소값
       answer = m
       break


print(answer)