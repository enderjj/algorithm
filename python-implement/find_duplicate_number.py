'''
给定一个长度为 n 的数组，其中的数字都是在 0 ~ n - 1 范围内，找到数组中任意一个重复的数字
'''

# 解法一：先对数组进行排序，然后重头到尾扫描数组，如果存在当前元素与前一个元素相等，就找到了重复的元素；否则继续往后查找


def find_duplicate_num1(alist):
    duplicate_num = -1  # 保存重复的数字
    alist.sort()  # 对数组进行排序
    print(alist)
    pre_num = alist[0]
    for i in range(1, len(alist)):
        if alist[i] == pre_num:
            duplicate_num = pre_num
        else:
            pre_num = alist[i]
    if duplicate_num == -1:
        print("数组中不存在重复的数字")
    return duplicate_num

# 解法二：利用一个新的数组来存放数字，新数组对应下标存放与下标相同的数字，如果当前要存放的数字对应的下标已有数字，则说明找到了重复的数字


def find_duplicate_num2(alist):
    duplicate_num = -1
    count = len(alist)
    blist = alist[:]
    # 新数组初始化
    for i in range(count):
        blist[i] = -1

    for num in alist:
        if blist[num] == num:
            duplicate_num = num
            break
        blist[num] = num
    if duplicate_num == -1:
        print("数组中不存在重复的数字")
    return duplicate_num

# 解法三：将数组中的数字进行排序，数字放到对应下标位置，如果下标已存在相同的元素，就说明找到了重复的数字
def find_duplicate_num3(alist):
    duplicate_num = -1
    count = len(alist)
    for i in range(count):
        num = alist[i]
        if num > count - 1:
            print("数组中存在元素大于列表长度")
            return
        while num != i:
            if alist[num] == num:
                duplicate_num = num
                return duplicate_num
            else:
                alist[num], alist[i] = num, alist[num]
                num = alist[i]
                if num > count - 1:
                    print("数组中存在元素大于列表长度")
                    return
    if duplicate_num == -1:
        print("数组中不存在重复的数字")
    return duplicate_num

# a = [4, 1, 2, 0, 3, 2, 1]
# print(find_duplicate_num3(a))

b = [1, 2, 3]
print(find_duplicate_num3(b))
