lista=[1,1]
while len(str(lista[-1])) < 1000:

  lista.append(lista[-1]+lista[-2])
  

print("El numero elegido tiene como indice",len(lista),"y tiene",len(str(lista[-1])),"cifras")