# MY CODE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l==l[::-1]


# BEST CODE
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=[]
        while head:
            s.append(head.val)
            head = head.next
        s_len = len(s)
        for i in range(s_len//2):
            if s[i]!=s[s_len-i-1]:
                return False
        return True

