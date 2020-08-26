# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = l1
        temp = 0
        while l1.next and l2.next:
            l1.val += l2.val + temp
            temp = 0
            if l1.val >= 10:
                temp += 1
                l1.val -= 10
            l1 = l1.next
            l2 = l2.next
        l1.val += l2.val + temp
        l1.next = l1.next or l2.next
        while l1.val >= 10:
            l1.val -= 10
            if not l1.next:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1
            l1 = l1.next
        return res