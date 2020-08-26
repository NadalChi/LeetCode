# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        temp = 0
        count = 0
        i = 0
        while p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
                count = 1
            elif count == 1:
                return self.deleteDuplicates(p.next)
            elif p.next.next != None:
                if p.next.val == p.next.next.val:
                    p.next = p.next.next
                    temp = 1
                else:
                    if temp == 1:
                        p.next = p.next.next
                        temp = 0
                    else:
                        p = p.next
            else:
                if temp == 1:
                    p.next = None
                    temp = 0
                else:
                    p = p.next
            i += 1
        if count == 1:
            return None
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        