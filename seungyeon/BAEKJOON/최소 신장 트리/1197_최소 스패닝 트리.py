import sys,heapq
input=sys.stdin.readline

v,e=map(int,input().split())
arr=[]
for i in range(e):
    a,b,c=map(int,input().split())
    arr.append((a,b,c))

arr.sort(key=lambda x : x[2])

parent = [i for i in range(v+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)


answer = 0
for a,b,cost in arr:
    if not same_parent(a,b):
        union_parent(a,b)
        answer += cost

print(answer)