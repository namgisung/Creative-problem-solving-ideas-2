import heapq

def dijkstra(layer1, layer2, start, goal):
    n = len(layer1)
    m = len(layer1[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 시간 정보를 무한대로 초기화: 시간을 알수 없음
    times = [[[float('infinity')] * m for _ in range(n)] for _ in range(2)]
    times[0][start[0]][start[1]] = 0

    queue = [(0, 0, start[0], start[1])]  # (시간, 층, x, y)

    while queue:
        time, layer, x, y = heapq.heappop(queue)

        if (layer, x, y) == goal:
            return time

        # 같은 층에서 한 칸씩 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                next_time = time + 0.5
                if (layer == 0 and layer1[nx][ny] != 'X' and next_time < times[layer][nx][ny]) or (layer == 1 and layer2[nx][ny] != 'X' and next_time < times[layer][nx][ny]):
                    times[layer][nx][ny] = next_time
                    heapq.heappush(queue, (next_time, layer, nx, ny))

        # 층을 변경할 경우
        if layer == 0 and layer2[x][y] != 'X' and time + 5 < times[1][x][y]:
            times[1][x][y] = time + 5
            heapq.heappush(queue, (time + 5, 1, x, y))
        elif layer == 1 and layer1[x][y] != 'X' and time + 5 < times[0][x][y]:
            times[0][x][y] = time + 5
            heapq.heappush(queue, (time + 5, 0, x, y))

    return -1

# 입력된 미로와 시작 위치, 도착 위치
stages = [
    [
    "XXXXXXXXXXXXX",
    "X,,,,,X,,,,,X",
    "X,XXX,X,XXX,X",
    "X,,OX,X,,,X,X",
    "XXX,X,XXX,X,X",
    "X,,,X,,,,,X,X",
    "X,XXXXXXXXX,X",
    "X,,,,,X,,,,,X",
    "XXXXX,X,XXX,X",
    "X,,,,,X,,-X,X",
    "X,XXXXXXXXX,X",
    "X,,,,,,,,,,,X",
    "XXXXXXXXXXXXX"
    ],
    [
    "XXXXXXXXXXXXX",
    "X,,,,,,,X,,,X",
    "X,,,X,X,X,,,X",
    "X,,,X,X,,,,,X",
    "X,XXX,X,X,XXX",
    "X,,,,,X,X,,,X",
    "XXXXX,XXX,,,X",
    "X,,,,,X,,,,,X",
    "X,XXXXXXXXX,X",
    "X,,,X,,,,,,,X",
    "X,X,X,X,XXX,X",
    "X,X,,,X,,,X,X",
    "XXXXXXXXXXXXX"        
    ]
]

start = (3, 3)  # 'O' 위치 (1층)
goal = (0, 9, 9)  # '-' 위치 (1층)

result = dijkstra(stages[0], stages[1], start, goal)
print("최소 시간:", result)
