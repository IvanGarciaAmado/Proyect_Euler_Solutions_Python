
lis=[]
res=0
contador=0
largo=[]
def main(n):
  contador=0
  lis=[]
  while n != 1:
    lis.append(int(n))
    if n%2==0:
      n=n/2
    else:
      n=3*n+1
  for i in range(len(lis)):
    contador=contador+1

  res=contador
 # print(c,"como de largo es",res)
 # print("lis",lis)
  largo.append(res)
c=0


while c<1000000:
  c=c+1
  #print(c/10000)
  main(c)
  

print("la cadena mas larga es de:",max(largo))
print("El indice de ese valor es:", largo.index(max(largo))+1)