lst = ['0','1','2','5','6','8','9']

a = int(input()) 
new_lst = lst.copy()
n = a - 6
i = 1
while n > 0:
    for j in range(len(lst)):
        out = new_lst[i] + lst[j]
        new_lst.append(out)
        n = n - 1
    i += 1
    if i == len(lst):
        i = 1

print(new_lst[a])

