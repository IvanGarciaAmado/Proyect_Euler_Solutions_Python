

primos=[2,3,5,7,11,13]
c=1
while c < 2000000:
  prim=0
  c= c+2
  for p in primos:
    if p != c:
      if c%p == 0:
        break
      else:
        prim= prim+1
        if prim == len(primos):
          primos.append(c)
          print("Ha transcurrido ",c/20000,"% el ultimo primo es ",c, "Hay un total de ", len(primos), "primos en la lista")

print(sum(primos))