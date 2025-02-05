#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(1, n+2):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

def cache_input(func):
    def wrapper(self, head, n):
        self.cache = head
        return func(self, head, n)
    return wrapper