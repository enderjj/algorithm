# 用两个栈实现队列
class TwoStackQueue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []
    
    # 插入元素
    def append_element(self, value):
        self.stack_one.append(value)

    # 删除元素
    def delete_element(self):
        delete_ele = None
        if len(self.stack_two) == 0:
            if len(self.stack_one) == 0:
                print("队列中没有元素，无法进行删除操作")
            else:
                while len(self.stack_one) != 0:
                    ele = self.stack_one.pop()
                    self.stack_two.append(ele)
                delete_ele = self.stack_two.pop()
        else:
            delete_ele = self.stack_two.pop()
        return delete_ele

que = TwoStackQueue()
que.append_element(1)
que.append_element(2)
que.append_element(3)
print(que.stack_one)
print(que.stack_two)
print(que.delete_element())
print(que.stack_one)
print(que.stack_two)
