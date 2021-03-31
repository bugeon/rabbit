import sys, copy

sys.setrecursionlimit(10**6)

def is_visited(v):
  if visited[v] == 0:
    visited[v] = 1
    print(v, end = ' ')

def dfs(node_info, v):
  print(v, end = ' ')
  for i in range(1, n + 1):
    if node_info[v][i] == 1 and visited[i] == 0:
      visited[i] = 1
      dfs(node_info, i)

def bfs(node_info, que):
  while len(que) != 0:
    v = que.pop(0)
    is_visited(v)
    for i in range(1, n + 1):
      if node_info[v][i] == 1:
        node_info[v][i] = 0
        node_info[i][v] = 0
        que.append(i)


n, m, v = map(int, sys.stdin.readline().split())

arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  p1, p2 = map(int, sys.stdin.readline().split())
  arr[p1][p2] = 1
  arr[p2][p1] = 1

copied_arr = copy.deepcopy(arr)
visited = [0] * (n + 1)
# stk = []
# stk.append(v)
visited[v] = 1
dfs(copied_arr, v)

print()

copied_arr = copy.deepcopy(arr)
visited = [0] * (n + 1)
que = []
que.append(v)
bfs(copied_arr, que)