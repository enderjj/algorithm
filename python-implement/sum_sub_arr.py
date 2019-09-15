'''
求连续子数组的最大和
数组中的数字可以是正数，也可以是负数
'''
def sum_sub_array(alist):
    if alist == None or len(alist) == 0:
        return
    
    max_sum = cur_sum = alist[0]
    start = 0
    end = 0
    count = len(alist)

    for i in range(1, count):
        val = alist[i]
        cur_sum += val
        if cur_sum < 0:
            cur_sum = 0
            start = i + 1
        elif max_sum < cur_sum:
            max_sum = cur_sum
            end = i
    
    print("从 %s 到 %s 的和最大，和为 %s" % (start, end, max_sum))

a = [1, -2, 3, 10, -4, 7, 2, -5]
sum_sub_array(a)
b = [-1, -1, -1, -1, -1]
sum_sub_array(b)
