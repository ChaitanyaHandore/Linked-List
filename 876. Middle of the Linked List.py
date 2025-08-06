# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cslow = head
        cfast = head
        
        while cfast and cfast.next:
            cslow = cslow.next
            cfast = cfast.next.next
        
        return cslow
