import sys
from collections import deque
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,k=map(int,input().split())

arr=[0] * 100001
move=[0] * 100001

# 1초후에 x-1,x+1
# 순간이동 2*x
# n -> k 인데 가장 빨리 가는 방법

def path(x):
    answer=[]
    tmp = x
    for _ in range(arr[x] + 1):
        answer.append(tmp)
        tmp = move[tmp]
    print(' '.join(map(str,reversed(answer))))


def bfs(tmp):

    que=deque()
    que.append(tmp)

    while que:
        tmp = que.popleft()

        if tmp == k:
            print(arr[tmp])
            path(tmp)
            return 
        
        for i in (tmp+1,tmp-1,tmp*2):
            if 0 <= i <= 100000 and arr[i] == 0:
                que.append(i)
                arr[i] = arr[tmp] + 1
                move[i] = tmp

answer = bfs(n)
