class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        # step1: 快指针先走n步
        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next

            # step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while fast:
            slow, fast = slow.next, fast.next

            # step3: 删除节点，并重新连接
        slow.next = slow.next.next
        return dummy.next
