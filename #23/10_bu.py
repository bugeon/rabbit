import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
  l = int(sys.stdin.readline().rstrip())
  board = [[False] * l for _ in range(l)]
  start_x, start_y = map(int, sys.stdin.readline().split())
  board[start_x][start_y] = True
  night = deque([(start_x, start_y, 0)])
  destination_x, destination_y = map(int, sys.stdin.readline().split())
  
  while night:
    current = night.popleft()
    if current[0] == destination_x and current[1] == destination_y:
      print(current[2])
      break
    # 나이트의 이동
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for move in moves:
      next_x, next_y = current[0] + move[0], current[1] + move[1]
      if next_x >= 0 and next_x < l and next_y >= 0 and next_y < l and board[next_x][next_y] == False:
        board[next_x][next_y] = True
        night.append((next_x, next_y, current[2] + 1))

