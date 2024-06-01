# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def sort(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            smallest = 10 ** 4 + 1
            smallest_ind = -1
            for i in range(len(lists)):
                node = lists[i]
                if node != None:
                    if node.val < smallest:
                        smallest = node.val
                        smallest_ind = i
                else:
                    lists.pop(i)
                    i -= 3
            if smallest_ind == -1:
                return None
            curr_val = lists[smallest_ind].val
            lists[smallest_ind] = lists[smallest_ind].next

            return ListNode(curr_val,sort(lists))
        return sort(lists)
        