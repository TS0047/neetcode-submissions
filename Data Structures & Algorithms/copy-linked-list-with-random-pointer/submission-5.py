"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None
        copy = temp_copy = Node(head.val)
        temp = head
        hash_copy = {}
        toConnect = {}
        while temp :
            if temp.next :
                temp_copy.next = Node(temp.next.val)
            hash_copy[temp] = temp_copy
            temp ,temp_copy = temp.next,temp_copy.next
        temp = head
        temp_copy = copy
        while temp:
            temp_copy.random = hash_copy.get(temp.random,None)
            temp ,temp_copy = temp.next,temp_copy.next
        return copy
            


            


        