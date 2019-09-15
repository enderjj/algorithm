# 实现 pow 函数
def base_pow(base, exp):
    if base == 0 and exp < 0:
        print("参数不合法")
        return 0
    elif base == 0:
        return 0
    else:
        new_exp = abs(exp)
        pow_result = compute_pow(base, new_exp)
        if exp < 0:
            result = 1 / pow_result
        else:
            result = pow_result
    return result


'''
计算 base 的 exp 次幂
1）exp == 0：结果为 1
2）exp == 1：结果为 base
3）exp > 1：如果 exp 为偶数，则结果为 base 的 exp / 2 次幂相乘；如果 exp 为奇数，则结果为 base 的 exp / 2 次幂相乘再乘以 base
4）用位移运算代替乘除，可以提高运算效率
'''


def compute_pow(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        res = compute_pow(base, exp >> 1)
        res *= res
        if exp & 1 == 1:
            res *= base
    return res


print(base_pow(2, 5))
print(base_pow(2, -5))
print(base_pow(2, 0))
print(base_pow(-2, 5))
print(base_pow(0, 5))
print(base_pow(0, -5))
