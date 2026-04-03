# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        temp = 0
        p1, p2 = l1, l2
        while p1 or p2 or temp:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            curr.next = ListNode(val1 + val2 + temp)
            if curr.next.val >= 10:
                curr.next.val = val1 + val2 - 10 + temp
                temp = 1
            else:
                temp = 0
            curr = curr.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        return dummy.next

            

            