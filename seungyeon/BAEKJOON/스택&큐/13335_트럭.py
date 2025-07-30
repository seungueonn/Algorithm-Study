# import sys
# input = sys.stdin.readline

# from collections import deque
# deq = deque()

# n, w, l = map(int, input().split()) # W : 다리 길이 , L : 다리 하중 
# arr = list(map(int, input().split()))

# for _ in range(w) :
#     deq.append(0)

# now = 0 # 현재 다리 위의 무게
# count = 0

# while len(arr) > 0 :
#     truck = arr[0]

#     check = deq.popleft()

#     if check != 0 :
#         now -= check

#     if (now + truck) <= l :
        
#         deq.append(truck)
#         now += truck
        
#         count += 1
#         arr.pop(0)
    
#     else :
#         deq.append(0)

#         count += 1

# while len(deq) > 0 :
#     deq.popleft()
#     count += 1

# print(count)

# 다리를 건너는 최대 
from collections import deque
import sys
input=sys.stdin.readline


n,w,l=map(int,input().split())
# n개 트럭, w 대 트럭 동시에 (단위길이) , l 최대하중

arr=list(map(int,input().split()))

que=deque([0] * w) # 다리 크기


index=0
time = 0
cur_w = 0

while index < n:

    time += 1
    out = que.popleft()
    cur_w -= out

    if cur_w + arr[index] <= l:
        que.append(arr[index])
        cur_w += arr[index]
        index += 1
    else:
        que.append(0)

time += w # 마지막 트럭이 건너는 시간

print(time)