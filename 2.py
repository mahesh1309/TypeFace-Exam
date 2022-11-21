first = input()
second = input()
ch = second[len(second)-1]
count = 0
for i in range(len(first)):
    if first[i] == ch:
        count += 1

print(f'last char of str2 is {ch} and it appeared {count} times in str1')