# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def rec(cur: Optional[ListNode], seen : set)-> bool:
            if cur is None :
                return False
            if cur in seen:
                return True
            seen.add(cur)
            return rec(cur.next,seen)
        return rec(head,set())