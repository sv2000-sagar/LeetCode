# Time: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head):
            return head
        tail = head
        length = 1
        # Get Length
        while(tail.next):
            length+=1
            tail = tail.next
        k = k % length
        if(k == 0): return head
        cur = head
        # move to the pivot and rotate
        for i in range(0,length-k-1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead