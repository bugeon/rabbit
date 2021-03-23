def DnC(his):
    if len(his) == 0:
        return 0
    if len(his) == 1:
        return his[0]
    
    l_2 = int(len(his)/2)
    temp1 = his[:l_2]
    temp2 = his[l_2:]
    cand = his[l_2]
#     print(temp1,temp2,cand)
    if len(his)>2 and his[l_2+1]>his[l_2-1]:
        for idx in range(1,l_2+1):
            cand = max(cand, len(his[l_2:l_2+1+idx])*min(his[l_2:l_2+1+idx]))
#             print(cand)
        for idx in range(l_2+1):
            cand = max(cand, len(his[l_2-idx:])*min(his[l_2-idx:]))
#             print(cand)
    else:
        for idx in range(1,l_2+1):
            cand = max(cand, len(his[l_2-idx:l_2+1])*min(his[l_2-idx:l_2+1]))
#             print(cand)
        for idx in range(l_2+1):
            cand = max(cand, len(his[:l_2+idx])*min(his[:l_2+idx]))
#             print(cand)
    answer = max(cand,DnC(temp1),DnC(temp2))
    return answer 

while 1:
    tc = input()
    if tc == '0':
        break
    else:
        heights = list(map(int,tc.split()[1:]))
        print(DnC(heights))