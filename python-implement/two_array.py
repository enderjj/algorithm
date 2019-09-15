# 二维数组中查找是否存在某个数字
def find_number(arr, key):
    row = len(arr) - 1
    col = len(arr[0]) - 1
    start_row = 0
    find = False
    while col >= 0 and start_row <= row:
        num = arr[start_row][col]
        if num == key:
            find = True
            break
        elif num > key:
            col -= 1
        else:
            start_row += 1
    return find

arr = [
  [1, 2, 8, 9],
  [2, 4, 9, 12],
  [4, 7, 10, 13],
  [6, 8, 11, 15]
]

print(find_number(arr, 3))
