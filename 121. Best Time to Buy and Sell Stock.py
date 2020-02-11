
#define the first flag
def find_best_time_brute(array):
    max=0
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            earn=array[j]-array[i]
            if earn>max:
                max=earn
    return max

def find_best_time_onepath(array):
    min_price=array[0]
    profit=0
    for i in range(0,len(array)):
        if array[i]<min_price:
            min_price=array[i]
        else:
            profit=max(profit,array[i]-min_price)
    return profit







if __name__ == '__main__':
    print(find_best_time_onepath([1,2,4,5]))

