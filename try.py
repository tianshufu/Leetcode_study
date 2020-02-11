#定义一个累成函数




a=[[1],[2,3],[4,5]]
b=[]
for i in range(0,len(a)):
    print(i,a[i])
    b.append(a[len(a)-i-1])

print(a[1])
print(b)