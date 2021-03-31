def dnc(tc):
    if len(tc) == 0:
        return (0, 0)
    if len(tc) == 1:
        return (tc[0], tc[0])
    
    l2 = int(len(tc)/2)
    t1 = tc[:l2]
    t2 = tc[l2:]
#     if len(tc) == 2:
#         return max(dnc(t1),dnc(t2), (sum(tc),min(tc)), key = lambda x: x[0]*x[1])
    
    candsum, candmin = sum(tc[l2-1:l2+1]),min(tc[l2-1:l2+1])
#     print(tc[l2+1], tc[min(l2-2,0)])
    if len(tc) >= 3 and tc[l2+1] > tc[max(l2-2,0)]:
        for idx in range(1,l2+1):
            tsum = sum(tc[l2-1:l2+1+idx])
            tmin = min(tc[l2-1:l2+1+idx])
            if candsum*candmin < tsum * tmin:
                candsum, candmin = tsum, tmin
        for idx in range(1,l2):
            tsum = sum(tc[l2-1-idx:])
            tmin = min(tc[l2-1-idx:])
            if candsum*candmin < tsum * tmin:
                candsum, candmin = tsum, tmin
            
    else:
        for idx in range(1,l2):
            tsum = sum(tc[l2-1-idx:l2+1])
            tmin = min(tc[l2-1-idx:l2+1])
            if candsum*candmin < tsum * tmin:
                candsum, candmin = tsum, tmin
        for idx in range(1,l2+1):
            tsum = sum(tc[:l2+1+idx])
            tmin = min(tc[:l2+1+idx])
            if candsum*candmin < tsum * tmin:
                candsum, candmin = tsum, tmin
#     print(t1,t2,(candsum,candmin))
    answer = max(dnc(t1),dnc(t2), (candsum,candmin), key = lambda x: x[0]*x[1])
#     print(t1,t2,answer)
    return answer 

input()
num_array = list(map(int,input().split()))
ans = dnc(num_array)
print(ans[0]*ans[1])