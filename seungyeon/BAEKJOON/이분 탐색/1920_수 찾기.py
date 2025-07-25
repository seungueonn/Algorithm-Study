# n=int(input())
# a=list(map(int,input().split(" ")))
# a.sort()

# m=int(input())
# arr=list(map(int,input().split(" ")))


# def binary(k):

#     l = 0
#     r = n-1

#     while(l <= r):
#         mid = (l+r) // 2

#         if k > a[mid]:
#             l = mid + 1
#         elif k < a[mid]:
#             r = mid - 1
#         else:
#             l = mid
#             r = mid
#             break

#     if l == mid and r == mid:
#         print(1)
#     else:
#         print(0)


            

# for i in range(len(arr)):
#     binary(arr[i])


# # n=int(input())
# # a=set(map(int,input().split(" ")))
# # m=int(input())
# # arr=list(map(int,input().split(" ")))

# # for i in arr:
# #     if i not in a:
# #         print('0')
# #     else:
# #         print('1')

import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
arr=list(map(int,input().split()))


# arr이 a에 존재하는지


def find(x):
    l,r=0,len(a)-1

    while l<=r:
        mid = (l + r) // 2

        if a[mid] == x:
            return True
        
        elif a[mid] < x :
            l = mid + 1

        elif a[mid] > x :
            r = mid - 1

    return False


for i in arr:
    if find(i):
        print(1)
    else:
        print(0)