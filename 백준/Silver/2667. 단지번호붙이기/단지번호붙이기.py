"""
Link : https://www.acmicpc.net/problem/2667


1. Main Idea
- Find the different groups in the 2D grid 
- DFS (Recursion)


2. Time Complexity
- O(V+E) = 5*49 ~ N^2
- V = n^2 = 49
- E = 4 * n^2 = 4*49


3. Data Structure
- 2 Conditions (Number==1 && Not Visited)
  => Call Recursion (DFS)
- Save the value to a list (각 단지의 집의 수를 저장)
- Sort the list (오름차순)

- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]

4. Output 
- 첫째줄 : 단지수
- 둘째줄~ : 각 단지내 집의 수 (오름차순)

"""

import sys
input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]
result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y,x):
   global each
   each += 1
   for k in range(4):
        nexty = y + dy[k]
        nextx = x + dx[k]
        if 0 <= nexty < n and 0 <= nextx < n:
            if map[nexty][nextx] == 1 and chk[nexty][nextx] == False:
                chk[nexty][nextx] = True
                dfs(nexty, nextx)

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True

            # DFS로 크기 (각 단지내 집의 수) 구하기 
            each = 0
            dfs(j,i)
            result.append(each)

            # 크기를 결과에 넣고, 오름차 순으로 정렬 

result.sort()
print(len(result))
for i in result:
    print(i)