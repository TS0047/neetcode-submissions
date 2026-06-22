# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the head anchor
        dummy = ListNode()
        curr = dummy
        
        a = list1
        b = list2
        
        # 2. Loop runs while BOTH lists still have remaining nodes
        while a is not None and b is not None:
            if a.val > b.val:
                curr.next = b  # Link the smaller node to our merged list
                b = b.next     # Move forward in list b
            else:
                curr.next = a  # Link the smaller node to our merged list
                a = a.next     # Move forward in list a
            
            curr = curr.next   # Advance our tracking pointer
            
        # 3. Append the remaining portion of whichever list is left over
        if a is not None:
            curr.next = a
        else:
            curr.next = b
            
        # Return the actual merged head (skipping the dummy)
        return dummy.next
