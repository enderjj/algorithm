# 从尾到头打印单链表的值

# 链表节点的定义
class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_link_node(phead):
    pnode = phead
    if pnode.next != None:
        print_link_node(pnode.next)        
    print(pnode.value)

node_head = pre_node = LinkNode(-1)
for i in range(5):
    node = LinkNode(i)
    pre_node.next = node
    pre_node = node

print_link_node(node_head)
