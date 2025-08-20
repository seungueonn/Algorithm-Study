import sys
input=sys.stdin.readline

# a에는 속하면서 b에는 속하지 않는 원소 

n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()

def binary(x):

    l,r=0,len(b)-1

    while l<=r:

        mid= (l+r)//2

        if b[mid] < x:
            l = mid + 1
        
        elif b[mid] == x:
            return False
        
        else:
            r = mid - 1

    return True

answer=[]
check=False
for i in a:
    if binary(i):
        answer.append(i)
        check=True

if answer :
    print(len(answer))
    answer.sort()
    print(*answer)
else:
    print(0)
    


