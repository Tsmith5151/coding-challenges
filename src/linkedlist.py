#Linked List
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  
        self.next = next #
        
    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    
    def __init__(self):
        pass
    
    def __repr__(self) -> str:
        _list = self.traverse_linked_list(self.results)
        _list.append("None")
        return ' -> '.join([str(i) for i in _list])
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ Merge two sorted list"""
        dummy = temp = ListNode(0)
        while l1 != None and l2 != None: 

            if l1.val < l2.val: 
                temp.next = l1 
                l1 = l1.next 
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 or l2 
        self.results = dummy.next 

    def traverse_linked_list(self, val=None, results =[]) -> List:
        """ Format Linked List"""
        if val == None:
            return
        results.append(val.val)
        self.traverse_linked_list(val.next)
        return results


if __name__ == '__main__':
    
    # List 1
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(10)
    e = ListNode(15)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # List 2
    A = ListNode(-1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    A.next = B
    B.next = C
    C.next = D

    solution = Solution()
    results = solution.mergeTwoLists(a,A)