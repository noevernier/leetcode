#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res1 = list1
        res2 = list2

        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            res2.next = self.mergeTwoLists(list1, list2.next)
            return res2
        else:
            res1.next = self.mergeTwoLists(list1.next, list2)
            return res1

        