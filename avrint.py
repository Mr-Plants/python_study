#get numberlist average
def avg(list):
    length=len(list)
    if length==0:
        return 0
    else:
        avgint=sum(list)/float(length)
        return avgint

n=int(raw_input("please input how much number you want count:"))
intlist=[]
i=0
while i<n:
    m=int(raw_input('please input a integer:'))
    if m<0:
        print 'need a positive integar!'
    else:
        intlist.append(m)
        i+=1
avgint=avg(intlist)
print 'you have input %d integers and they are:' %(n)
print intlist
print 'their average is: '+str(avgint)
