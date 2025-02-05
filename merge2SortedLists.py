#https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Create a dummy node.
        tail = dummy  # This will be the end of the merged list.

        while l1 and l2:
            # Compare the values at l1 and l2, then move the tail and selected pointer forward.
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next  # Move the tail pointer forward.

        # Attach the remaining elements from l1 or l2.
        tail.next = l1 if l1 else l2

        return dummy.next  # Return the merged list, excluding the dummy node.