import sys
from collections import deque

computers = int(sys.stdin.readline())
network = [[0] * (computers + 1) for _ in range(computers + 1)]
visited = [False] * (computers + 1)
for _ in range(int(sys.stdin.readline())):
	c1, c2 = map(int, sys.stdin.readline().split())
	network[c1][c2] = 1
	network[c2][c1] = 1

visited[1] = True
injected = 0
que = deque([1])
while que:
	c = que.popleft()
	# print(c, end=' ')
	for i in range(1, computers + 1):
		if network[c][i] == 1 and visited[i] == False:
			visited[i] = True
			que.append(i)
			injected += 1

print(injected)


# from sys import stdin
# read = stdin.readline
# dic={}
# for i in range(int(read())):
#     dic[i+1] = set()
# for j in range(int(read())):
#     a, b = map(int,read().split())
#     dic[a].add(b)
#     dic[b].add(a)

# def dfs(start, dic):
#     for i in dic[start]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, dic)
# visited = []
# dfs(1, dic)
# print(len(visited)-1)
