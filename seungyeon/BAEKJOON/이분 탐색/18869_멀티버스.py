import sys
input=sys.stdin.readline

m,n=map(int,input().split())

arr=[]
for i in range(m):
    arr.append(list(map(int,input().split())))

cnt = 0

for planet in range(m):
    for i in range(m):
        arr_sort = sorted(arr[i]) # 입력받은 행성 정렬
        index = []
        for j in arr[i]:
            index.append(arr_sort.index(j) + 1 ) # arr_sort는 각 행성의 크기별 순서 값 저장해둠
        arr[i] = index

for i in range(m-1):
    for j in range(i+1,m):
        if arr[i] == arr[j]:
            cnt += 1

print(cnt)
