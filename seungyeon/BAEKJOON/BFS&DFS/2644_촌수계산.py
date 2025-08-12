import sys
input=sys.stdin.readline

n=int(input())
a,b=map(int,input().split())

m=int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split()) # 부모,자식
    graph[y].append(x)
    graph[x].append(y)

visited=[False]*(n+1)
result=[]
def dfs(v,num): # a 부모 b 자식

    print(result)
    num += 1

    visited[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i,num)


dfs(a,0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)