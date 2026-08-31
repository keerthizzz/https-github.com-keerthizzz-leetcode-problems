# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            nxt = kth.next
            p, cur = nxt, prev.next

            while cur != nxt:
                temp = cur.next
                cur.next = p
                p, cur = cur, temp

            temp = prev.next
            prev.next = kth
            prev = temp