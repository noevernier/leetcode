# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        reverse_list = None
        current_head = head
        while current_head:
            temp = current_head.next
            current_head.next = reverse_list
            reverse_list = current_head
            current_head = temp
        return reverse_list
