
arr=[]
def rotate(arr):
    y,x=len(arr),len(arr[0])
    rotated_arr=[[0] * x for _ in range(y)]

    for i in range(y):
        for j in range(x):
            rotated_arr=[j][-1-i] = arr[i][j]

    return rotated_arr

arr.append((list(input().strip()))) # str을 한개씩 배열에 저장하는 방법


for i in range(Y):
    count += arr[i].count(0) # 배열에서 특정 숫자 카운트


min_value=int(1e9) # 최소값 초기화하는 최대값



arr=[[0] * 5 for _ in range(4)]
arr=[1,2,3,4,1,2,3,1,2,1]

d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)


print(list(map(int,d.values())))

# dict value 기준 
arr=sorted(d.items(),key=lambda x: x[1])
print(arr)

# dict key 기준 
arr=sorted(d.items(),key=lambda x: x[0])
print(arr)


s = set()
for i in arr:
    s.add(i)
print(s)


arr=[1,3,5,7,2,4,6,8]
arr.sort(reverse=True)
print(arr)

arr=[(0,9),(1,8),(2,7),(3,6),(4,5)]
arr = sorted(arr,key = lambda x : -x[0])
print(arr)
arr = sorted(arr,key = lambda x : x[1])
print(arr)

arr=[(0,9),(1,9),(2,7),(3,6),(4,5)]
arr = sorted(arr,key = lambda x : (x[1],-x[0]))
print(arr)

