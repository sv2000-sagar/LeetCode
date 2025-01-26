# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time: O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        # creating offset of n b/w left and right
        while(n>0 and right):
            right = right.next
            n-=1
        # left -> node before deleted node
        while(right):
            left = left.next
            right = right.next
        # Delete Node
        left.next = left.next.next
        return dummy.next