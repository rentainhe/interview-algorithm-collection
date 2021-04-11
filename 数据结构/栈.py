"""
原始的python的列表就是可以作为栈操作
stack = []
stack.append() 入栈,在末尾添加一位元素
stack.pop() 出栈,末尾元素送出
"""


class Stack(object):
    def __init__(self, limit=10):
        # limit 来限制栈中最多能装多少元素
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print("StackOverFlowError")
            pass
        self.stack.append(data)

    def pop(self):
        # 首先要判断栈是否为空
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        # 要注意判断stack中有没有元素
        # stack = []
        # bool(stack) = False
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        # 如果一个列表为空, 那么 bool(list)=False
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


# Practice 1
# 字符串匹配问题

if __name__ == "__main__":
    def balanced_parentheses(parentheses):
        stack = Stack(len(parentheses))
        for i in parentheses:
            if i == '(':
                stack.push(i)
            elif i == ')':
                if stack.is_empty():  # 如果已经是空的，就返回False，这里考虑到可能 ( 的数量比 ) 少
                    return False
                stack.pop()
        return stack.is_empty()


    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
