# import sys

# input=sys.stdin.readline


# def get_parent(x):
#     if x == parent[x]:
#         return parent[x]
    
#     return get_parent(parent[x])

# def is_same_parent(a,b):
#     return get_parent(a) == get_parent(b)

# def union_parent(a,b):
#     a = get_parent(a)
#     b = get_parent(b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

 


# n,m=map(int,input().split())
# # arr=[[] for i in range(n+1)]
# arr=[]
# parent=[i for i in range(n+1)]
# for i in range(m):
#     a,b,c=map(int,input().split())
#     arr.append((c,a,b))

# arr.sort()

# answer = []
# for cost,x,y in arr:
#     if not is_same_parent(x,y):
#         union_parent(x,y)
#         answer.append(cost)

# answer.sort()
# print(sum(answer[0:-1]))

import sys
input=sys.stdin.readline

n,m=map(int,input().split())

arr=[]
for i in range(m):
    a,b,c=map(int,input().split())
    arr.append((c,a,b))

arr.sort() #유지비용이 짧은 노드부터 이어가며 모든 노드를 다 잇는다. 가장 나중에 이은 노드를 뺀다

parent = [ i for i in range(n+1)] #부모를 자기 자신으로 초기화

def get_parent(x):

    if x == parent[x]:
        return parent[x]
    
    return get_parent(parent[x])

def is_same_parent(a,b):
    return get_parent(a) == get_parent(b)


def union(a,b):

    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer=0
last=0
for cost,x,y in arr:

    if not is_same_parent(x,y):
        union(x,y)
        answer += (cost)
        last = cost

print(answer-last)