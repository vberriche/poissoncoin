import numpy as np
import matplotlib.pyplot as plt

l = 13
e = 2.71828182846

def f(n):		# factoriel f(n) = n!
	if(n>1):
		return n*f(n-1)
	else:
		return 1

# 10 DOGE = 10 PSC		1st day
# 10 DOGE = 1 PSC			last day

# Chart of Poisson distribution for l = 13

poisson = []

for n in range(0,26):
	p = l**n * e**(-l) / f(n) 
	poisson += [p]

x = [ k for k in range(len(poisson)) ]

# Distribution of tokens

amount = []

m = .0001*l**l * e**(-l) / f(l)

for n in range(l-1,l+8):

	p = round(l**n * e**(-l) / ( f(n) * m ))

	amount += [p]		# per 3 days
	amount += [p]
	amount += [p]

amount += [1000,1000,1000]

print(amount)

j = [ k for k in range(len(amount)) ]

plt.subplot(2, 1, 1)
plt.plot(x, poisson, '.-')
plt.plot([l-1,l-1],[0,poisson[l-1]],"k--")
plt.plot([l+8,l+8],[0,poisson[l-1]],"k--")

plt.title("Poisson distribution and distribution of PoissonCoin")

plt.ylabel('P(X=k), lambda = 13')
#plt.xlabel('k')

plt.subplot(2, 1, 2)
plt.plot([0,0],[0,10000],"k--")
plt.plot([len(amount)-1,len(amount)-1],[0,10000],"k--")
plt.plot(j, amount, 'o-')
plt.xlabel('n-th day of the IFO')
plt.ylabel('Amount of tokens for 1000 DOGE')
plt.ylim((0,11000))

#plt.savefig('distribution.png')

plt.show()
