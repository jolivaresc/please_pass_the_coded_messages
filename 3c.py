a=[3, 1, 4, 1]
f=[3, 1, 4, 1, 5, 9]
c=[3, 1, 4, 1, 5, 9,1,3,4,6,1,4,3,8,2,4,6,8]
g=[5,4,7,8,1,2,0]
gg=[1,2,3]
d=[5,8,1,2]
b=[3, 1, 4, 1, 5, 9,4,6,4,2]
c1=[1,1,1,1,1,1,1]
k=[1,1]
from collections import deque
def answer(L):
	if len(L) < 100 and not any(n < 0 for n in L):
		if sum(L) % 3 == 0:
			return int(''.join(map(str,sorted(L,reverse=True))))
		elif sum(L) % 3 != 0:
			mul  = sorted([i for i in L if i % 3 == 0])
			nmul = sorted([i for i in L if i % 3 != 0])
			tmp = deque(nmul)
			f=[]
			g=[]
			if nmul:
				for i in nmul:
					tmp.rotate(1)
					g=list(tmp)
					if sum(g[0:len(nmul)-1]) % 3 == 0:
						f.append(sorted(g[0:len(nmul)-1],reverse=True))
				if not mul and not f:
					return 0
				elif not f:
					return int(''.join(map(str,sorted(mul,reverse=True))))
				else:
					return int(''.join(map(str,sorted(max(f)+mul,reverse=True))))
			elif mul: 
				return int(''.join(map(str,sorted(mul,reverse=True))))
			else: return 0
	else: return 0



print answer([3, 1, 4, 1])


