# # # 집합안에 포함되는 세수의 합인데 가장 큰거 

# # import sys
# # input=sys.stdin.readline

# # n=int(input())
# # arr=[]
# # for i in range(n):
# #     arr.append(int(input().rstrip()))

# # l,r=0,0
# # sum=0
# # arr_set=set(arr)

# # answer=[]
# # while(True):

# #     if r >n-1 or l >r : 
# #         break
    
# #     if sum == arr[r]:
# #         answer.append(sum)
# #         sum -= arr[l]
# #         l += 1
    
 
# #     sum += arr[r]
# #     r+= 1

# # answer.sort()

# # if n==0:
# #     print(0)
# # else:
# #     print(answer[-1])



# import sys
# input=sys.stdin.readline

# answer = 0
# n = int(input())
# arr=[int(input()) for _ in range(n)]

# arr.sort()
# arr2=list()

# for i in range(n):
#     for j in range(i,n):
#         arr2.append(arr[i]+arr[j])

# print(arr2)
# arr2.sort()

# for i in range(n):
#     for j in range(i,n):
#         num = arr[j] - arr[i]
#         start = 0
#         end = len(arr2) - 1


#         while start <= end:
#             mid = (start+end)//2

#             if num > arr2[mid]:
#                 start = mid + 1
#             elif num < arr2[mid]:
#                 end = mid-1
#             else:
#                 answer=max(answer,arr[j])
#                 break

# print(answer)



# import sys
# sys.setrecursionlimit(100000000)
# input=sys.stdin.readline

# n=int(input())
# arr=[]
# visited=[0] * n
# for _ in range(n):
#     arr.append(int(input().strip()))


# # 3수 구하기
# answer=[]
# max_num = 0
# def back(depth,idx):

#     global max_num

#     # 가장 큰거 
#     if depth == 3:
#         x = sum(answer)

#         if binary(x):
#             max_num=max(x,max_num)

#     for i in range(idx,n):
#         if not visited[i]:
#             visited[i] = True
#             answer.append(arr[i])
#             back(depth+1,i)
#             answer.pop()
#             visited[i] = False


# # # 3수의 합 찾기 

# def binary(x):
#     l,r=0,n-1

#     while l <= r:

#         mid = (l+r)//2

#         if arr[mid] == x:
#             return True
        
#         elif arr[mid] > x:
#             r = mid -1
#         else:
#             l = mid + 1

#     return False

# back(0,0)
# print(max_num)



def binary(x):

    global result 
    l,r=0,len(arr2)-1

    while l <= r:

        mid = (l+r)//2

        if arr2[mid] == x:
            result=max(result,arr[mid])
            return True
        
        elif arr2[mid] > x:
            r = mid -1
        else:
            l = mid + 1

    return False

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr2 = []
for i in range(n):
    for j in range(i, n):
        arr2.append(arr[j] + arr[i])

arr2.sort()
result = 0 

for i in range(n): # z
    for j in range(i,n): # k 
        a = arr[j] - arr[i] # x + y = " k - z "
        start = 0
        end = len(arr2)-1

        while start <= end: # x+y의 집합에서 k-z 찾기 

            mid = (start+end) //2
            
            if a > arr2[mid]:
                start = mid + 1
            elif a < arr2[mid]:
                end = mid - 1
            else:
                result = max(result ,arr[j]) # k넣기 
                break


print(arr2)
print(result)