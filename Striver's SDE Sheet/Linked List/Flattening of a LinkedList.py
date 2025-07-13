# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

# Time: O(NlogK)
# Space: O(k)

class Solution:
    def flattenLinkedList(self, head):
        if not head:
            return None
        
        # Step 1: Collect all head nodes of child lists
        lists = []
        curr = head
        while curr:
            lists.append(curr)
            curr = curr.next

        # Step 2: Use mergeKLists logic to flatten
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                mergedList.append(self.merge2Lists(l1, l2))
            lists = mergedList

        return lists[0]
    
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.child = l1
                l1 = l1.child
            else:
                tail.child = l2
                l2 = l2.child
            tail = tail.child
        if l1:
            tail.child = l1
        if l2:
            tail.child = l2
        return dummy.child