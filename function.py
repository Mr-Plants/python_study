#function
def max1(a,b):
    if a>=b:
        return a
    else:
        return b

#c=max1(1,2)
#print c

def avg_number(number_list):
    length=len(number_list)
    sum=0
    for i in range(0,length):
        sum+=number_list[i]
    return sum/length

list_a=[10,14,16,30]

#print avg_number(list_a)
    
