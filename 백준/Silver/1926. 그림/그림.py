

"""

Link : https://www.acmicpc.net/problem/1926

1. Main Idea
- Find the number of paintings and the size of the largest painting in a given grid
- BFS
- Double for loop, True when new painting is found

2. Time Complexity
- O(V+E) = 5*m*n
- V = m*n
- E = 4*V 

3. Data Structure
- Total Graph : int[][]
- Visited : boolean[][]
- Queue(BFS) : int[]

4. Output 
- 첫째줄 : 그림의 개수
- 둘째줄 : 가장 넓은 그림 개수 
"""

# Preset

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
graph =  [list(map(int, input().split())) for _ in range(n)]
chk = [[False]* m for _ in range(n)]




total_count = 0
max_count = 0

dRow = [-1, 0, 1, 0]
dColumn = [0, 1, 0, -1]


def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dRow[k]
            nx = ex + dColumn[k]
            if 0<=ny<n and 0 <=nx<m:
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs 



for j in range(n):
    for i in range(m):
        if graph[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True    
            
            # 전체 그림 개수를 + 1
            total_count += 1
            
            # BFS > 그림크기를 구하기 
            max_count = max(max_count, bfs(j,i))
            
            # 최대값을 기록하기 (두번째 Output)
            
            

            # When BFS is done 
print(total_count)
print(max_count)
