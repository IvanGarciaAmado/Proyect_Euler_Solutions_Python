

sumsqr= 0
sqrsum=0
sum = 0
for i in range(1,101,1):
  sumsqr= sumsqr + i*i
for j in range(1,101,1):
  sum=sum+j
sqrsum= sum*sum
print(sumsqr)
print(sqrsum)

print(-sumsqr+sqrsum)