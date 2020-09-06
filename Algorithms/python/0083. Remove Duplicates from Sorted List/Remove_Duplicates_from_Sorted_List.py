# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        #print(head)
        while p.next != None:
            #print(p,p.val,p.next,p.next.val)
            if p.val == p.next.val:
                p.next = p.next.next
                #print(p,p.val,p.next,p.next.next)
            else:
                p = p.next
            
            #print('\n')
        return head
        #print(head)
        """
        :type head: ListNode
        :rtype: ListNode
        """