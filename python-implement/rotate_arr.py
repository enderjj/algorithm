# 查找旋转数组的最小数字
def find_min_number(alist):
    count = len(alist)
    if alist == None or count == 0:
        print("列表为空")
        return None
    start = 0
    end = count - 1
    min_num = alist[start]
    while alist[start] >= alist[end]:
        if end - start == 1:
            min_num = alist[end]
            break
        else:
            mid = (end + start) // 2
            if alist[start] == alist[end] and alist[start] == alist[mid]:
                min_num = find_by_order(alist, start, end)
                break
            else:
                if alist[mid] >= alist[start]:
                    start = mid
                elif alist[mid] <= alist[end]:
                    end = mid
    return min_num

def find_by_order(alist, start, end):
    min_num = alist[start]
    for val in alist:
        if val < min_num:
            min_num = val
    return min_num

# a = [3, 4, 5, 1, 2]
a = [1, 0, 1, 1, 1]
print(min(a))
print(find_min_number(a))
