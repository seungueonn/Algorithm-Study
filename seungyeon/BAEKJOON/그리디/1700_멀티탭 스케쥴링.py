
# from collections import deque,defaultdict
# import heapq

# n,k=map(int,input().split())
# arr=list(map(int,input().split()))

# arr_cnt=defaultdict(int)
# for a in arr:
#     arr_cnt[a] += 1

# # window를 heapque로 만들고 <사용 횟수, 번호> 넣고 사용횟수 작은걸로 정렬해서 -> heapq는 자동으로 작은걸로 정렬
# # window에 내가 원하는 값이 없다면 작은걸 빼낸다 이 때 cnt ++ 
# answer=0
# que=[]

# for i in arr:
#     print(que)
#     if len(que) < n:
#         if (arr_cnt[i],i) not in que:
#             heapq.heappush(que,(arr_cnt[i],i))
#     else:
#         if (arr_cnt[i],i) not in que:
#             heapq.heappop(que)
#             answer += 1
#             heapq.heappush(que,(arr_cnt[i],i))
            
#         else: # 콘센트 이미 있음 
#             continue

# print(answer)

# # https://magentino.tistory.com/88#google_vignette


import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))

tap=[]
answer=0

for i in range(k):
    if arr[i] in tap:
        continue

    if len(tap) < n:
        tap.append(arr[i])
        continue

    priority=[]

    for j in tap:
        if j in arr[i:]: # 다음에 또 이용한다면
            priority.append(arr[i:].index(j)) # 다음에 또 이용할 인덱스
        else:
            priority.append(101)

    target = priority.index(max(priority)) # 가장 나중에 사용할 값 타겟
    tap.remove(tap[target])
    tap.append(arr[i])
    answer += 1

print(answer)