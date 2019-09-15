'''
重新排列数组，将数组中的所有奇数都排在偶数的前面
'''
def resort(alist):
    if alist == None or len(alist) == 0:
        print("数组为空")
        return
    count = len(alist)
    start = 0
    end = count - 1
    while start < end:
        while start < end and alist[start] & 1 != 0:
            start += 1
        while start < end and alist[end] & 1 == 0:
            end -= 1
        if start < end:
            alist[start], alist[end] = alist[end], alist[start]
    return alist

a = [1, 2, 3, 4, 5]
print(resort(a))
