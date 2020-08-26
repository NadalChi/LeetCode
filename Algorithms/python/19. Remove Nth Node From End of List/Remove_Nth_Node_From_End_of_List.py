# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for i in range(n):
            slow = slow.next
        if not slow:
            return head.next
        while slow.next:
            fast, slow = fast.next, slow.next
        fast.next = fast.next.next
        return head