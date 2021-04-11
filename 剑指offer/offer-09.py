# 用两个栈实现队列操作
# 主要注意的是 append 和 pop的用法

class CQueue:

    def __init__(self):
        self.queue = []

    def appendTail(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead(self) -> int:
        if len(self.queue) !=0:
            x = self.queue[0]
            self.queue = self.queue[1:]
            return x
        else:
            return -1


class CQueue2:
    def __init__(self):
        self.queue = []
    def appendTail(self, value: int) -> None:
        self.queue.append(value)
    def deleteHead(self) -> int:
        if self.queue == []:
            return -1
        else:
            return self.queue.pop(0)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()