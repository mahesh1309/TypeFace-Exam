n = int(input())

out = ""
while n!=0:
    out += str(n%3)
    n = n //3

output = ""
for i in range(len(out)):
    output += out[len(out)-i-1]


print(output)