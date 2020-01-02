# -*- coding: utf-8 -*-
# tsp问题求解

city=['tangshan','beijing','tianjin','shijiazhuang','qinhuangdao','langfang']
cityNo=['A','B','c']

dist=((0,1,3,4,5),
        (1,0,1,2,3),
        (3,1,0,1,2),
        (4,2,1,0,1),
        (5,3,2,1,0))

# find all path O(n!)
def perm(city):
    #print(city)
    if len(city)<=1:
        return [city]
    r=[]
    for i in range(len(city)):
        s=city[:i]+city[i+1:]
        p=perm(s)
        #print p
        for j in p:
            #print j
            r.append(city[i:i+1]+j)
    return r

print perm(cityNo)
