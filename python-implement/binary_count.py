# 统计整数的二进制表示中，1 出现的次数
# 将整数减去 1 的结果与整数做与运算，就相当于把整数二进制表示中最右边的 1 变成 0
def count_binary(n):
    count = 0
    while n:
        count += 1
        n = (n - 1) & n
    return count

print(count_binary(5))
print(count_binary(-3))
