import sys

def power_matrix(a, b):
  result = [[0] * n for _ in range(n)]
  
  if b == 1:
    for i in range(n):
      for j in range(n):
        a[i][j] %= 1000
    return a
  elif b % 2 == 0:
    result = [[0 for _ in range(n)] for _ in range(n)]
    a = power_matrix(a, b//2)
    for i in range(n):
      for j in range(n):
        for k in range(n):
          result[i][j] += a[i][k] * a[k][j]
        result[i][j] %= 1000
    return result
  else:
    result = [[0 for _ in range(n)] for _ in range(n)]
    c = power_matrix(a, b - 1)
    for i in range(n):
      for j in range(n):
        for k in range(n):
          result[i][j] += c[i][k] * a[k][j]
        result[i][j] %= 1000
    return result

n, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = power_matrix(matrix, b)
for row in answer:
  print(*row)