#2017/10/1

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        tempnode = ListNode(0)
        tempnode.next = head
        while tempnode.next.next:
            if tempnode.next.val == tempnode.next.next.val:
                tempnode.next.next = tempnode.next.next.next
            else:
                tempnode.next = tempnode.next.next

        return (head)