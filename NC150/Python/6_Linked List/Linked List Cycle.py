# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# floyd tortoise and hare (Floyd's Cycle Finding Algorithm)
# Time: O(n)
# Space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow): return True
        return False