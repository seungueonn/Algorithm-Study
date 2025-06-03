# # 두 수의 합을 갱신하면서 가장 합을 작게 만들어야함

# n,m=map(int,input().split())
# arr=list(map(int,input().split()))

# # m번 한 뒤 남은 카드의 합

# arr.sort()
# for i in range(m):
#     sum = arr[0]+arr[1]
#     arr[0],arr[1] = sum,sum
#     arr.sort()

# answer =0
# for j in range(n):
#     answer += arr[j]
# print(answer)

import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr) # list to heapq

for _ in range(m):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sum_ab = a + b
    heapq.heappush(arr, sum_ab)
    heapq.heappush(arr, sum_ab)

print(sum(arr))