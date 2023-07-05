num=int(input())
summ=0
for i in range(1,num+1):
    if i%3!=0:
        summ=summ+i**3

print(summ)
summ1=0
count=0
while count!=num:
    count=count+1
    if count%3!=0:
        summ1 = summ1 + count ** 3
print(summ1)