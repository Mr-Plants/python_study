# coding=utf-8
# tsp问题求解
import random

city = ['tangshan', 'beijing', 'tianjin', 'shijiazhuang', 'qinhuangdao', 'langfang']
cities = ['A', 'B', 'C']
cityNo = [1, 2, 3, 4, 5]

dist = ((0, 1, 3, 4, 5),
        (1, 0, 1, 2, 3),
        (3, 1, 0, 1, 2),
        (4, 2, 1, 0, 1),
        (5, 3, 2, 1, 0))


# 找到所有路径组合 时间复杂度为：O(n!)
def perm(l):
    # 递归步骤：对每个城市，构造不包含这个城市的所有路径组合
    if len(l) > 1:
        r = []
        for i in range(len(l)):
            # 除本城市以外的其他城市的集合
            s = l[:i] + l[i + 1:]
            p = perm(s)
            for j in p:
                # 将路径组合（序列）与这个城市进行组合
                r.append(l[i:i + 1] + j)
        return r
    # 递归基础：一个城市只有一种排列，就是它本身
    else:
        return [l]


# print perm(cityNo)

# 随机选择一条路径
def randompath(inc):
    # 集合的拷贝
    allcity = inc[:]
    path = []
    loop = True
    while loop:
        tmp = random.choice(allcity)
        path.append(tmp)
        if len(allcity) == 1:
            loop = False
        else:
            allcity.remove(tmp)
    return path


def getminist(n):
    optimal = 1000000
    for i in range(n):
        d = distcal(randompath(cityNo), dist)
        if d < optimal:
            optimal = d
    return optimal


# 计算路径距离
def distcal(path, dist):
    pathlen = len(path)
    sumdist = 0
    for i in range(pathlen - 1):
        dis = dist[path[i] - 1][path[i + 1] - 1]
        sumdist += dis
    # 加上回家的距离
    backhomedis = dist[path[pathlen - 1] - 1][path[0] - 1]
    sumdist += backhomedis
    return sumdist


# todo 贪心算法

print getminist(10)
