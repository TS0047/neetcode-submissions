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
        if head is None:
            return None
        copy = Node(head.val)
        temp = head
        temp_copy = copy
        hash_copy = {}
        toConnect = {}
        while(temp is not None):
            if temp.next is not None:
                temp_copy.next = Node(temp.next.val)
            hash_copy[temp] = temp_copy
            if temp.random in hash_copy:
                temp_copy.random = hash_copy[temp.random]
            else:
                toConnect[temp_copy] = temp.random
            temp ,temp_copy = temp.next,temp_copy.next
        for i in toConnect:
            i.random = hash_copy.get(toConnect[i])
        return copy
            


            


        