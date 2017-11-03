#2017/11/2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ini = ListNode(0)
        ini.next = head

        prior = ini
        next = prior.next

        while next is not None:
            if next.val == val:
                prior.next = next.next
            else:
                prior = next
            next = prior.next

        return ini.next

