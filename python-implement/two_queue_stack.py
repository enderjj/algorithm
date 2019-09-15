# 两个队列实现栈
class TwoQueueStack:
    def __init__(self):
        self.queue_one = []
        self.queue_two = []
    
    # 插入元素
    def append_element(self, value):
        if len(self.queue_two) != 0:
            self.queue_two.append(value)
        else:
            self.queue_one.append(value)

    # 删除元素
    def delete_element(self):
        delete_ele = None
        len_one = len(self.queue_one)
        len_two = len(self.queue_two)
        if len_one != 0:
            for i in range(len_one - 1):
                ele = self.queue_one[i]
                self.queue_two.append(ele)
            delete_ele = self.queue_one[len_one - 1]
            self.queue_one = []
        elif len_two != 0:
            for i in range(len_two - 1):
                ele = self.queue_two[i]
                self.queue_one.append(ele)
            delete_ele = self.queue_two[len_two - 1]
            self.queue_two = []
        else:
            print("列表元素为空，无法删除元素")
        return delete_ele

stack = TwoQueueStack()
stack.append_element(1)
stack.append_element(2)
stack.append_element(3)
print(stack.queue_one)
print(stack.queue_two)
print(stack.delete_element())
print(stack.queue_one)
print(stack.queue_two)
print(stack.delete_element())
print(stack.queue_one)
print(stack.queue_two)
print(stack.delete_element())
print(stack.queue_one)
print(stack.queue_two)
print(stack.delete_element())
print(stack.queue_one)
print(stack.queue_two)

