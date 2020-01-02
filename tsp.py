# -*- coding: utf-8 -*-
# tsp问题求解

city = ['tangshan', 'beijing', 'tianjin', 'shijiazhuang', 'qinhuangdao', 'langfang']
cityNo = ['A', 'B', 'C']

dist = ((0, 1, 3, 4, 5),
        (1, 0, 1, 2, 3),
        (3, 1, 0, 1, 2),
        (4, 2, 1, 0, 1),
        (5, 3, 2, 1, 0))


# find all path O(n!)
def perm(l):
    # print(city)
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)
        # print p
        for j in p:
            # print j
            r.append(l[i:i + 1] + j)
    return r


print perm(cityNo)
