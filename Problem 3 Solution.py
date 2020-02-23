n=int(input())
c=0
s=bin(n)
a=s[2: ]
print(a)
b=str(a)
c=b.split("0")
d=max(c)
e=len(d)
print(e)
