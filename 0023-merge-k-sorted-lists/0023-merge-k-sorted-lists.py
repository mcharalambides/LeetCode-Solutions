# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return 
        
        heads = []
        for x in lists:
            if x:
                currentNode = x
                while currentNode:
                    heads.append(currentNode.val)
                    currentNode = currentNode.next
        
        if not heads:
            return None
        
        if len(heads) == 1:
            return ListNode(heads[0],None)
        heads.sort()
        head = ListNode(heads[0],None)
        currentNode = head
        for node in heads[1:-1]:
            currentNode.next = ListNode(node, None)
            currentNode = currentNode.next
        
        currentNode.next = ListNode(heads[-1],None)
        return head
        
        