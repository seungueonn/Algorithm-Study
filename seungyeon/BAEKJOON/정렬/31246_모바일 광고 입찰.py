import sys
input=sys.stdin.readline

n,k=map(int,input().split())

arr=[]
for i in range(n):
    a,b= map(int,input().split())
    arr.append(b-a)

arr.sort()

if arr[k-1] < 0:
    print(0)
else:
    print(arr[k-1])

