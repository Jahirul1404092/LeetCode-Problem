# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root=ListNode(-1)
        root.next=head
        node1=node2=root.next
        while node1 and node1.next:
                node2=node2.next
                node1=node1.next.next
        return node2
