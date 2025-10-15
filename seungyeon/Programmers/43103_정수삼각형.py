def solution(triangle):
    answer = 0
    # idx or idx+1
    
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
          
    for i in range(1,len(triangle)):
        n = len(triangle[i])
        for j in range(n):
            if j == n - 1 :
                dp[i][j] = dp[i-1][n-2] + triangle[i][j]
            elif j == 0:
                dp[i][0] = dp[i-1][j] + triangle[i][j]
            else :
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        
        
    return max(dp[-1])