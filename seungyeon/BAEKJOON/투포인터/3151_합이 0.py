
# # import sys
# # input=sys.stdin.readline

# # n=int(input().strip())
# # arr_input=list(map(int,input().split()))

# # # 합이 0이 되는 3인조
# # # arr.sort()

# # minus=[]
# # plus=[]
# # for i in range(n):
# #     if arr_input[i] < 0:
# #         minus.append((arr_input[i]))
# #     elif arr_input[i] > 0:
# #         plus.append((arr_input[i]))
# #     else:
# #         minus.append((arr_input[i]))
# #         plus.append((arr_input[i]))


# # answer = 0
# # minus.sort(reverse=True)
# # plus.sort()

# # print(minus)
# # print(plus)

# # def find(x,arr):

# #     global answer

# #     l,r=0,1

# #     while 0 <= l < r < len(arr): # 2개의 방법이면? 

# #         if arr[l] + arr[r] == x:
# #             # print(l,r,arr[l]+arr[r])
# #             print(arr[l],arr[r])

# #             answer += 1
# #             l += 1
    
# #         elif arr[l] + arr[r] > x:
# #             l -= 1

# #         elif arr[l] + arr[r] < x:
# #             r += 1
# #             # l += 1
        
# # #음수기준
# # for k in minus:
# #     find(-k,plus)

# # # 양수기준
# # for k in plus:
# #     find(-k,minus)
        
# # print(answer)


# # 세 팀원의 코딩 실력 합이 0
# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=list(map(int,input().split()))

# minus=[]
# plus=[]
# for i in arr:
#     if i < 0:
#         minus.append(i)
#     elif i > 0 :
#         plus.append(i)
#     else:
#         minus.append(i)
#         plus.append(i)

# minus.sort()
# plus.sort()


# def check(arr,k):

#     l,r=0,1

#     while l < r:

#         mid=l+r//2

#         if arr[l]+arr[r] < k:




# 코딩실력 합이 0
import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

arr.sort()


ans = 0

for i in range(n-2):
    
    l,r=i+1,n-1
    goal = -arr[i]
    mx_idx=n

    while l < r :
        tmp = arr[l]+arr[r]

        if tmp < goal:
            l += 1

        elif tmp == goal:
            if arr[l] == arr[r]: # 정렬되어있기 때문에 l,r 원소가 같으면 둘 사이 거리가 가능한 경우의 수
                ans += r - l
            else:
                if mx_idx > r:
                    mx_idx = r

                    while mx_idx>=0 and arr[mx_idx-1] == arr[r]:
                        mx_idx -= 1
                ans += r - mx_idx + 1
            l += 1

        else: # tmp > goal
            r -= 1

print(ans)

