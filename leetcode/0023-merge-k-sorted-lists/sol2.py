# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if l1 == None and l2 == None:
                return None
            elif l1 == None:
                return ListNode(l2.val, merge(l1, l2.next))
            elif l2 == None:
                return ListNode(l1.val, merge(l1.next, l2))
            
            if l1.val < l2.val:
                return ListNode(l1.val, merge(l1.next, l2))
            else:
                return ListNode(l2.val, merge(l1, l2.next))

        def divide(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists) == 0:
                return ListNode().next
            if len(lists) == 1:
                return lists[0]
            left = lists[:len(lists) // 2]
            right = lists[len(lists) // 2:]
            if len(left) == 1 and len(right) == 1:
                return merge(left[0], right[0])
            
            return merge(divide(left), divide(right))
        
        return divide(lists)
        