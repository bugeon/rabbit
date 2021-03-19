# n,m,k <= 100
A_n, A_m = map(int, input().split())
A_list = [list(map(int, input().split())) for _ in range(A_n)]    
B_m, B_k = map(int, input().split())
B_list = [list(map(int, input().split())) for _ in range(B_m)]

print(A_list)
print(B_list)

answer = [[0] * B_k for _ in range(A_n)]
for idx1 in range(A_n):
    for idx2 in range(B_k):
        for idx3 in range(A_m):
            answer[idx1][idx2] += A_list[idx1][idx3] * B_list[idx3][idx2]

# print(answer)
for ans in answer:
    print(*ans)