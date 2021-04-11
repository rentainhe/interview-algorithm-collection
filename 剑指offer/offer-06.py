# 从尾到头打印链表
# input [1,2,3] output [3,2,1]

def reversePrint(head):
    head = head[::-1]
    return head

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

# 对于链表节点来说 head.val 表示节点的值
# head.next 表示指向下一个节点


head = [1,2,3]
print(reversePrint(head))
