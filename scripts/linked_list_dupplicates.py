""" 
Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Reference:  https://leetcode.com/problems/remove-duplicates-from-sorted-list/


Solution: implement a nested loop (inner/outter) 
Time Complexity: O(N)
Memory Complexity: O(1)
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = head
    while cur:  # Outer Loop - exits when next node is null
        # Inner Loop
        while cur.next and cur.next.val == cur.val:  # if duplicates
            # update the pointer by skipping over the duplicate node
            cur.next = cur.next.next
        cur = cur.next
    return head


if __name__ == "__main__":
    # List
    head = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    head.next = b
    b.next = c

    print(deleteDuplicates(head))
