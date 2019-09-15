'''
找到单链表中倒数第 k 个节点
设置两个指针，其中一个指针先走 k - 1 步，然后两个指针同时走
当先走的指针指向最后一个节点时，后走的指针刚好指向倒数第 k 个节点
'''
def find_node(phead, k):
    if phead == None or k <= 0:
        return None
    pfirst = phead
    plast = phead
    for i in range(k - 1):
        if pfirst.next != None:
            pfirst = pfirst.next
        else:
            print("链表长度小于k")
            return None
    while pfirst.next != None:
        pfirst = pfirst.next
        plast = plast.next
    return plast.value

# 单链表定义
class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None
