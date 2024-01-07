# Definition for singly-linked list.
from typing import Optional

# Solution optimal in space

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        while head:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow and fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False