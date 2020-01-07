# coding=utf-8
# 测试指定随机数据得出的结果是否符合概率分布
import random

n = 10000
m = 0
for i in range(n):
    r = random.random()
    if r <= 0.5:
        m += 1

p = float(m) / float(n)

print '通过统计{0}个数据，落在0到0.5的概率为{1}'.format(n, p)
