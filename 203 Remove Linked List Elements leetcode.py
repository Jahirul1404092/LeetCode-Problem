# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        root=ListNode(-1)
        root.next=head
        current=root
        while root.next!=None:
            if root.next.val==val:
                root.next=root.next.next
            else:
                root=root.next
        return current.next
