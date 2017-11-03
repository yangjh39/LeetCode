# 2017/11/12

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        last = None
        now = head
        while now.next is not None:
            nex = now.next
            now.next = last
            last = now
            now = nex

        now.next = last

        return now