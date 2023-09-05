import mathlib as m
import random as r

with open("data.txt","r") as f:
    numbers=f.readlines()

for i in range(len(numbers)):
    numbers[i]=float(numbers[i])

sum1=0
sum2=0
for i in range(len(numbers)):
    sum2=m.add(sum2,numbers[i])
X=m.mul(m.div(1,len(numbers)),sum2)

for i in range(len(numbers)):
    sum1=m.add(sum1,m.pow(m.sub(numbers[i],X),2))

fract=m.div(1,m.sub(len(numbers),1))
("fract",fract)
sqr=m.mul(fract,sum1)
s=m.sqrr(sqr,2)
print(s)

