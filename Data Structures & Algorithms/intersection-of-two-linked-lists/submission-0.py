# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        pointer = headA
        while pointer:
            seen.add(pointer)
            pointer = pointer.next
        pointer = headB
        while pointer:
            if pointer in seen:
                return pointer
            pointer = pointer.next
        return None
