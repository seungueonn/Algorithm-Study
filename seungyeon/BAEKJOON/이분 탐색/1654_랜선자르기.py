# import sys
# input=sys.stdin.readline

# k,n=map(int,input().split())
# arr=[]
# for i in range(k):
#     arr.append(int(input().rstrip()))

# start,end=0,min(arr)
# while(start<=end):

#     mid = (start+end)//2
#     sum = 0
#     for i in arr:
#         sum += i//mid

#     if sum >= n:
#         start = mid +1
#     else:
#         end = mid - 1

# print(end)

# n개의 랜선 필요 
# k개의 오영식 랜선 -> n개의 같은 길이 랜선
# 최대 랜선 길이 

import sys
input=sys.stdin.readline

k,n=map(int,input().split())
arr=[]
for i in range(k):
    arr.append((int(input().strip())))


l,r=1,max(arr) # 제일작은게 1이면? 
answer=0

while l <= r:

    mid=(l+r)//2

    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid

    if cnt >= n:
        answer=max(mid,answer)
        l = mid + 1 

    else: # cnt < n: 갯수가 모자름 -> 자르는 숫자를 작게 해야함 
        r = mid - 1

     
print(answer)