# https://www.acmicpc.net/problem/7576 7576 토마토
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = -1

dq = deque()
unripe_tomato = 0
for i in range(n):
	for j in range(m):
		if box[i][j] == 1:
			dq.append([i, j, 0])
		elif box[i][j] == 0:
			unripe_tomato += 1

# 토마토 익기
	# 상하좌우 네 방향으로 뻗어나가기
dr = [ 1, 0, -1, 0]
dc = [ 0, 1, 0, -1]
while dq and unripe_tomato > 0:
	current = dq.popleft()
	x, y, day = current[0], current[1], current[2]
	answer = day + 1
	for i in range(4):
		next_x = x + dr[i]
		next_y = y + dc[i]
		if 0 <= next_x < n and 0 <= next_y < m and box[next_x][next_y] == 0:
			box[next_x][next_y] = 1
			unripe_tomato -= 1
			dq.append([next_x, next_y, day + 1])

# 전부 익지 못하는 상황이면 -1 출력
if unripe_tomato > 0:
	print(-1)
elif answer == -1:
	print(0)
else:
	print(answer)