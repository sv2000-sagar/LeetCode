# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        cycle = False
        # detecting cycle
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                cycle = True
                break
        # finding starting point
        cur = head
        res = None
        if(cycle):
            while(cur):
                if(cur == slow):
                    res = cur
                    break
                cur = cur.next
                slow = slow.next
        return res     