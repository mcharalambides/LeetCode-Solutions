# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or head.next == None:
            return head
        
        nodes = []
        currentNode = head
        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next
        
        k = k % len(nodes)
        for i in range(0,k):
            nodes[-2].next = None
            node = nodes.pop()
            nodes.insert(0,node)
            nodes[0].next = nodes[1]
        
        return nodes[0]