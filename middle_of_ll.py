# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        tmp = head
        while (tmp):
            count += 1
            tmp = tmp.next
        count //= 2
        while count:
            head = head.next
            count -= 1
        return head
