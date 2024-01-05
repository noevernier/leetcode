# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        test = head
        size = 0
        while test:
            size += 1
            test = test.next
        if size==1:
            return None
        if size-n==0:
            return head.next
        curr = head
        prev = None
        counter = 0
        while curr:
            if counter==size-n:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            counter+=1
        return head
        