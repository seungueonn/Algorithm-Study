import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]

adj=[[] for _ in range(n+1)]
indegree=[0] * (n+1)

for i in range(m):
    a,b=map(int,input().split()) # a < b
    adj[a].append(b)
    indegree[b] += 1

que =deque()
answer=[]
def sort_graph():

    # indegree가 0 이라면 
    for i in range(1,n+1):
        if indegree[i] == 0:
            que.append(i)
            
    while que:
        cur = que.popleft()
        answer.append(cur)
        for i in adj[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)


sort_graph()
print(*answer)


    



# 작은순으로 줄세운 결과 
