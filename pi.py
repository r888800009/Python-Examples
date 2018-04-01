#This script by r888800009

import random
from decimal import *

#Monte Carlo method
getcontext().prec = 10
inside=0
total=0
while total <10000000:
	x=Decimal(random.random())
	y=Decimal(random.random())

	r = x*x+y*y
	if r <=1:
		inside+=1.0
	#print(inside,r)
	total +=1.0
out =str(Decimal(inside) *Decimal(4)/ Decimal(total))
print(out)