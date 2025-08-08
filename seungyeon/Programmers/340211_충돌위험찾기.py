
def solution(points,routes):

    point_map = dict()
    for i in range(len(points)):
        point_map[i+1] = points[i]

    robots = []

    for route in routes:
        start_x,start_y = point_map.get(route[0])
        robots.append((start_x,start_y,route[::-1]))

    cnt = 0
    while robots:
        tmp_robots =[]
        robots_pos = dict()

        for robot in robots:
            x,y,route = robot

            if (x,y) in robots_pos:
                robots_pos[(x,y)] += 1
            else:
                robots_pos[(x,y)] = 1

            if [x,y] == point_map.get(route[-1]):
                route.pop()

            if route:
                to_x,to_y=point_map.get(route[-1])
                x,y=move(x,y,to_x,to_y)
                tmp_robots.append((x,y,route))

        cnt += sum( [1 if i >= 2 else 0 for i in robots_pos.values()])
        robots = tmp_robots
    return cnt

def move(x,y,to_x,to_y):
    if x > to_x:
        return (x-1,y)
    elif x < to_x:
        return (x+1,y)
    
    if y > to_y:
        return (x,y-1)
    elif y < to_y:
        return (x,y+1)
    
    return (x,y)