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
            
        length,cur = 1,head
        while(cur.next):
            length +=1
            cur = cur.next
        k = k % length
        if(k == 0):
            return head
        cur.next = head # last node -> first node
        pivot = length-k
        cur = head
        while(pivot > 1):
            cur = cur.next
            pivot -=1
        newHead = cur.next # pivot node next is newHead
        cur.next = None # pivot node next to null
        return newHead    