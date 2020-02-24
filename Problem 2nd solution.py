ls1 = eval(input())
k = len(str(max(ls1)))
ma = 0
ans = ''
l1 = []
print(ls1)
ls1 = [str(i) for i in ls1]
for h in range(len(ls1)):
    ma = 0
    for i in ls1:
        for j in ls1:
            if i != j and i not in l1:
                y = i + j
                y = int(y[:k])
                if y>ma:
                    ma = y
                    n = str(i)
    l1.append(n)
for i in l1:
    ans = ans+i
print(ans)




#or another code

a=[10,7,76,415]
from fractions import Fraction
arranged=sorted(a, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
done=""
for i in arranged:
	done=done+str(i)
print(done)
