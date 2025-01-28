# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Striver
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = None
        while(temp):
            kthNode = self.findKthNode(temp,k)
            if(not kthNode):
                if(prevNode):
                    prevNode.next = temp
                break
            nextNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)
            if(temp == head): # first Group (no prev)
                head = kthNode # kth node is the new head after reversing 
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode
        return head
        

    def findKthNode(self,temp,k):
            cur = temp
            while(cur and k > 1):
                cur = cur.next
                k-=1
            return cur

    def reverse(self,head):
        cur = head
        prev = None
        while(cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev