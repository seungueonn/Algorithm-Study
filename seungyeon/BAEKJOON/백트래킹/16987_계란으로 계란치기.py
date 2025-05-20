import sys
input=sys.stdin.readline

n=int(input())

arr=[]
for i in range(n):
    a,b=map(int,input().split()) # 내구도,무게
    arr.append([a,b])


visited=[False] * n

max_value=0


def check(arr):
    cnt = 0
    for i in arr:
        if i[0] <= 0:
            cnt += 1
    return cnt 

def dfs(index,arr):

    global max_value

    visited[index] = True

    if index == n-1:
        max_value=max(max_value,check(arr))
        return 
    
    # 현재 들고 있는 계란이 깨졌을 때 
    if arr[index][0] <= 0:
        dfs(index+1,arr)

    else:
        isBroken = True

        for i in range(index,n):
            if index != i and arr[i][0] > 0 : # visited를 이용한 단순 방문 확인이 아님
                isBroken = False
                arr[i][0] -= arr[index][1]
                arr[index][0] -= arr[i][1]

                
                dfs(index+1,arr) # 선택

                arr[i][0] += arr[index][1]
                arr[index][0] -= arr[i][1]

        if isBroken:
            dfs(n,arr)
                

dfs(0,arr)
print(max_value)