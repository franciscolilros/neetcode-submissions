# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        dummy = head
        
        temp = []

        for i, a in enumerate(lists):
            if a:
                heapq.heappush(temp, (a.val, i))
        
        while temp:
            tempList = heapq.heappop(temp)
            index = tempList[1]
            node = lists[index]
            head.next = node
            head = head.next

            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(temp, (lists[index].val, index))
        
        return dummy.next