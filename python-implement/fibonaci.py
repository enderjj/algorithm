''' 
斐波那契数列
f(n) = f(n-1) + f(n-2)
'''
def fibonaci(n):
    recur_list = [0, 1]
    if n <= 1:
        return recur_list[n]
    for i in range(2, n+1):
        recur_list.append(recur_list[i - 1] + recur_list[i - 2])
    return recur_list[len(recur_list) - 1]

print(fibonaci(100))
