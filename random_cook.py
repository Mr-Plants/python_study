# coding=utf-8
# 练习random模块函数

import random

# 产生一个0-1的随机浮点数
print random.random()

# 产生一个指定范围内的浮点数
print random.uniform(1, 2)

# 产生一个指定范围内的整数
print random.randint(0, 100)

# 从有序序列中随机选择一个元素
a = [1, 3, 5, 7, 9]
print random.choice(a)

# 将一个有序序列随机打乱
b = [1, 2, 3, 4, 5]
random.shuffle(b)
print b

# 将一个有序序列随机截取指定长度片段（非连续），也可以理解为从指定序列中选择n个
c = [1, 2, 3, 4, 5]
print random.sample(c, 2)
