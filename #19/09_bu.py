import sys

while True:
  n, *heights = map(int, sys.stdin.readline().split())
  heights.append(0)

  if n == 0:
    break
  
  s = []
  max_area = 0
  for i, h in enumerate(heights):
    while s and heights[s[-1]] > h:
      ih = heights[s.pop()]
      w = i - s[-1] - 1 if s else i
      area = w * ih
      if max_area < area:
        max_area = area
    s.append(i)
  print(max_area)
