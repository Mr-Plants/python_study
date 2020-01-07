# coding=utf-8
# 使用蒙特卡洛算法求解圆周率pi

# int只能将整数字符串或浮点数转换
import math
import random

n = int(float(raw_input('请输入需要模拟的次数：\n')))

m = 0

for i in range(n):
    x, y = random.random(), random.random()
    if math.sqrt(x ** 2 + y ** 2) < 1.0:
        m += 1

my_pi = float(m) / float(n) * 4

prec = abs(my_pi - math.pi) / math.pi

print '共模拟{0}次，计算圆周率为{1}，误差为{2}'.format(n, my_pi, prec)


# 什么操作，不懂
def get_pi():
    n = 100000
    p = sum(1 if random.random() ** 2 + random.random() ** 2 < 1 else 0 for i in range(n)) * 4.0 / n
    print p


get_pi()
