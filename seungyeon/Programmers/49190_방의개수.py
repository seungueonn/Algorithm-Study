def solution(arrows):
    answer = 0
    
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[1,1,0,-1,-1,-1,0,1]
    
    x,y=0,0
    
    visited_node = set()
    visited_node.add((x,y))
    
    route = set()
    cycle = 0
    
    for arrow in arrows:
        
        for _ in range(2):
            nx,ny=x + dx[arrow] , y + dy[arrow] 
            if (nx,ny) in visited_node  and  (x,y,nx,ny) not in route:
                answer += 1
                
            route.add((x,y,nx,ny))
            route.add((nx,ny,x,y))
            
            visited_node.add((nx,ny))
            x,y=nx,ny
            
    
    
    return answer