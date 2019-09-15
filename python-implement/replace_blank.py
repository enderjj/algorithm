# 将字符串中的空格替换成 %20
def replace_blank(ss):
    count = len(ss)
    blank_count = 0
    for s in ss:
        if s == " ":
            blank_count += 1
    if blank_count == 0:
        return ss
    else:
        add_len = 2 * blank_count # 需要增加的长度
        new_count = count + add_len # 替换后字符串的总长度
        for i in range(add_len):
            ss = ss[:len(ss)] + " "
        i = count - 1
        j = new_count - 1
        while i >= 0 and j >= 0 and i != j:
            if ss[i] != " ":
                ss = ss[:j] + ss[i] + ss[j+1:]
                j -= 1
            else:
                ss = ss[:j-2] + "%20" + ss[j+1:]
                j -= 3
            i -= 1
    return ss

ss = "we are happy"
# print(replace_blank(ss))
print(ss.replace(" ", "%20"))
