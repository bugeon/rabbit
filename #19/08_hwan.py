# dp = [0,1]
# n = int(input())
# for _ in range(n-1):
#     if n >= 2:
#         dp.append((dp[-1]+dp[-2])%1000000007)


# print(dp)

# from collections import deque
# n = int(input())
# dq = deque()
# dq.extend([0,1])
# # dq = [0,1]
# for num in range(n):
#     if num >= 1:
#         dq.append((dq.popleft()+dq[-1])%1000000007)
# answer = 0 if n == 0 else dq[-1]
# print(answer)

# def matmul(mat1,mat2):
#     answer = [[0] * len(mat2[0]) for _ in range(len(mat1))]
#     for idx1 in range(len(mat1)):
#         for idx2 in range(len(mat2[0])):
#             for idx3 in range(len(mat1[0])):
#                 answer[idx1][idx2] += mat1[idx1][idx3] * mat2[idx3][idx2]%1000000007
#     return answer

# def squared(mat, n):
#     if n <2:
#         return mat
#     if n%2 == 0:
#         return matmul(squared(mat,n/2),squared(mat,n/2))
#     else : 
#         return matmul(mat,matmul(squared(mat,(n-1)/2),squared(mat,(n-1)/2)))

# mat = [[1,1],[1,0]]
# n = int(input())
# ans = squared(mat,n)
# print(ans[0][1])

def matmul(mat1,mat2,n):
    global mat_d
    answer = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    for idx1 in range(len(mat1)):
        for idx2 in range(len(mat2[0])):
            for idx3 in range(len(mat1[0])):
                answer[idx1][idx2] += mat1[idx1][idx3] * mat2[idx3][idx2] %1000000007
    return answer

def squared(mat, n):
    global mat_d
    if n in mat_d:
        return mat_d[n]
    if n%2 == 0:
        mat_d[n] = matmul(squared(mat,n//2),squared(mat,n//2),n//2)
        return mat_d[n]
    else : 
        mat_d[n] = matmul(mat,matmul(squared(mat,(n-1)//2),squared(mat,(n-1)//2),(n-1)//2),1)
        return mat_d[n]
    
mat_d = dict()
mat = [[1,1],[1,0]]
mat_d[1] = mat
n = int(input())
ans = squared(mat,n)
print(ans[0][1]%1000000007)
