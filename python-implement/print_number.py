'''
输入数字 n，打印从 1 开始到最大的 n 位数结束的所有数字
'''
def print_number(n):
    list_num = []
    for i in range(n):
        list_num.append(0)
    while not increment(list_num):
        print_num(list_num)

# 实现列表模拟加 1 操作
def increment(alist):
    over_flag = False
    more_flag = False
    count = len(alist)
    for i in range(count - 1, -1, -1):
        if i == count - 1:
            sum = alist[i] + 1
        else:
            sum = alist[i] + more_flag
        
        if sum >= 10:
            more_flag = True
            sum = sum - 10
        else:
            more_flag = False
        alist[i] = sum
        if i == 0 and more_flag:
            over_flag = True
    return over_flag

# 模拟打印数字，数字前面的 0 不打印，从第一个非 0 数字开始打印
def print_num(alist):
    count = len(alist)
    print_flag = False
    for i in range(count):
        if not print_flag and alist[i] != 0:
            for val in alist[i:]:
                print(val)
            # print(alist[i:])
            return


print(print_number(2))
