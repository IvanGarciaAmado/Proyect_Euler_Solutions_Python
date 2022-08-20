list = [1,2]
res = 0
while max(list) < 4000000:
  a= max(list)
  del list[-1]
  b = max(list)
  del list[-1]
  list.append(b)
  list.append(a)
  list.append(a+b)

for i in list:
  if i%2 == 0:
    res = res + i
  else:
    continue

print(res)