ma = 0
a = int(input())
ls1 = []
c = 0
str1 = bin(a)
for i in str1[2:]:
    if i == '1':
        c = c+1
    if i == '0':
        if c > ma:
            ls1.append(c)
            c = 0
    if c == len(str1)-2:
        ls1.append(c)
print(max(ls1))
