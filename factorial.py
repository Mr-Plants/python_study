# coding=utf-8
# 求解阶乘算法

# 递归求解，复杂度是 O(n!)
def fact(n):
    # 递归步骤：当n>1是 n! = n * (n-1)!
    if n > 1:
        x = fact(n - 1)
        return x * n
    # 递归基础：1! = 1
    else:
        return 1


# 迭代求解，复杂度是O(n)
def fact2(n):
    product = 1
    for i in range(1, n):
        product = product * i
    return product * n


print fact(19)
print fact2(3)
