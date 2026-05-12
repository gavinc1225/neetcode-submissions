# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head

        while curr:
            tmp = curr.next # store the next node in tmp
            curr.next = prev # curr.next gets flipped
            prev = curr # prev becomes curr
            curr = tmp # curr becomes next
            '''
            essentially you are flipping the arrow and moving through the list
            '''
        return prev
        

        

        