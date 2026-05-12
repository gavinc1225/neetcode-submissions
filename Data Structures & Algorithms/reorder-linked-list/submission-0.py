# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
find middle of linked list using fast and slow pointers
reverse the second half
alternate adding new node to list
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # prev is head of second half 

        # alternate
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second # alternate starting with first half
            second.next = tmp1 # set to next of first half
            first, second = tmp1, tmp2 # move both forward
        

        

        
        

