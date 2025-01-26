# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""Iterative
Time: O(n) Space: O(1)"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,cur = None,head
        while(cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

"""Recursive
Time: O(n) Space: O(n)"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversedHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedHead