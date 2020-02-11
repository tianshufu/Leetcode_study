#定义一个累成函数
def get_value(n):
    if(n==0):
        return 1
    if (n==1):
        return 1
    else:
        return n*get_value(n-1)
#定义组合函数
def combination_num(m,n):
    if (n==0):
        return 1
    else:
        return (int(get_value(m)/(get_value(n)*get_value(m-n))))

#定义产生第i行的函数
def generate_n(i):
    list_return=[]
    num=i-1
    for i in range(0,num+1):
        list_return.append(combination_num(num,i))
    return list_return
#定义产生所有数的函数
def generate_all(n):
    list_start=[]
    for i in range(1,n+1):
        list_start.append(generate_n(i))
    return list_start




if __name__ == '__main__':
    print(generate_n(1))
    print(generate_all(5))