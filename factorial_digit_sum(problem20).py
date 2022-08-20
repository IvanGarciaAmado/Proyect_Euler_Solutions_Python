
def factorial(n):
  c=1
  for i in range(n,0,-1):
    c=c*i
  return(c)

numero=factorial(100)
c=0
for i in str(numero):
  c=c+int(i)
print(c)