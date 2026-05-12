# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        head = dummy
        carry = 0

        while l1 and l2:
            value = l1.val + l2.val + carry
            if value < 10:
                new_node = ListNode(value, None)
                dummy.next = new_node
                carry = 0
            else:
                new_node = ListNode(value % 10, None)
                dummy.next = new_node
                carry = 1
            l1, l2 = l1.next, l2.next
            dummy = dummy.next
        

        if l1:
            while l1:
                value = l1.val + carry
                new_node = ListNode(value % 10, None)
                carry = value // 10
                dummy.next = new_node
                dummy = dummy.next
                l1 = l1.next
        elif l2:
            while l2:
                value = l2.val + carry
                new_node = ListNode(value % 10, None)
                carry = value // 10
                dummy.next = new_node
                dummy = dummy.next
                l2 = l2.next
        
        if carry == 1:
            new_node = ListNode(1, None)
            dummy.next = new_node

        return head.next
