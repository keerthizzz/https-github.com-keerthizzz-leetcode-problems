
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
    
        curr.next = list1 if list1 else list2
        
        return dummy.next


def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


list1 = build_list([1,2,4])
list2 = build_list([1,3,4])
sol = Solution()
merged = sol.mergeTwoLists(list1, list2)
print(to_list(merged))  
