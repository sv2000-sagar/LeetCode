# Time: O(n)
# Spact: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # finding middle (splitting list in 2 halfs)
        fast,slow = head.next,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        # reversing second half of the list
        prev, curr = None, second
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

    # merging both lists
        first, second = head, prev #(prev is starting node of second list)
        while(second): # nodes in list 2 may be less than list 1
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            