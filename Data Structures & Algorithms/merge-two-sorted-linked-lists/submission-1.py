# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        
        a = list1
        b = list2
        
        # 2. Loop runs while BOTH lists still have remaining node
        while a is not None and b is not None:
            if a.val > b.val:
                curr.next = b  
                b = b.next     
            else:
                curr.next = a  
                a = a.next     
            
            curr = curr.next   
            
        
        if a is not None:
            curr.next = a
        else:
            curr.next = b
            
        
        return dummy.next
