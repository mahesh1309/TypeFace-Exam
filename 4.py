# temp = [-1]*256
# mat = [temp]*256

mat = [[1,0,0,1,1],[1,0,0,0,1],[1,0,0,1,1],[1,1,1,1,1]]

lt = [255,255]
rt = [255,0]
lb = [0,255]
rb = [0,0]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            if lt[0] > i:
                lt[0] = i
            if lt[1] > j:
                lt[1] = j
            if rt[0] > i:
                rt[0] = i
            if rt[1] < j:
                rt[1] = j
            if lb[0] < i:
                lb[0] = i
            if lb[1] > j:
                lb[1] = j
            if rb[0] < i:
                rb[0] = i
            if rb[1] < j:
                rb[1] = j

if lt[1] != lb[1]:
    lt[1] = min(lt[1],lb[1])
    lb[1] = min(lt[1],lb[1])
if lt[0] != rt[0]:
    lt[0] = min(lt[0],rt[0])
    rt[0] = min(lt[0],rt[0])
if rt[1] != rb[1]:
    rt[1] = max(rt[1],rb[1])
    rb[1] = max(rt[1],rb[1])
if lb[0] != rb[0]:
    lb[0] = max(lb[0],rb[0])
    rb[0] = max(lb[0],rb[0])


print(lt,rt,lb,rb)
            

