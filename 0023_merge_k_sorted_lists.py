#https://leetcode.com/problems/merge-k-sorted-lists/description/

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a dummy node and a tail pointer.
        dummy = ListNode()
        tail = dummy

        # Create a list to store the current node of each list.
        current = [node for node in lists]

        while any(current):
            # Find the index of the minimum value.
            min_val = float('inf')
            min_index = -1
            for i, node in enumerate(current):
                if node and node.val < min_val:
                    min_val = node.val
                    min_index = i
            # Move the tail pointer and the selected pointer forward.
            tail.next = current[min_index]
            tail = tail.next
            current[min_index] = current[min_index].next

        return dummy.next


def mergeTwoLists(l1, l2):
    # Initialize a prehead that helps in simplifying edge cases
    prehead = ListNode(-1)
    prev = prehead

    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    # Exactly one of l1 and l2 can be non-null at this point, so connect
    # the non-null list to the end of the merged list.
    prev.next = l1 if l1 is not None else l2

    return prehead.next


def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None

    # Iteratively merge lists two by two
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeTwoLists(l1, l2))
        lists = mergedLists

    return lists[0]
