
a=6
b=2
res,resto=divmod(a,b)
print(res,resto)

from math import sqrt
divisores=[]
c=0
n=1
def comprobar(c): 
  for i in range(round(sqrt(c)),1,-1):
    res,resto=divmod(c,i)
    if resto==0:
      divisores.append(i)
      divisores.append(res)

  if len(set(divisores)) > 500:
    print("Listo ",c ,set(divisores), len(set(divisores)))

contador=1

while len(set(divisores)) <500:
  divisores.clear()
  c=c+contador
  contador += 1
  comprobar(c)

76576500