
list=[]
lista=[]
listb=[]
for i in range(100,999,1):
  for j in range(999,100,-1):
    multi= i*j
    for o in str(multi):
      lista.append(o)
    for p in reversed(lista):
      listb.append(p)
    if lista == listb:
      list.append(multi)
    lista.clear()
    listb.clear()

print(max(list))

lista=[]
listb=[]
for i in range(10):
  lista.append(i)
print(lista)
for k in reversed(lista):
  listb.append(k)
print(listb)