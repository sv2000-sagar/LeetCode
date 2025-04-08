# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head.next,head
        # finding middle
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        # reversing second half of the list
        prev = None
        while(second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # check pali
        left,right = head,prev
        while(right):
            if(left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True