""" 
Reverse Linked List

Reference: https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """
    Two pointers
    :type head: ListNode
    :rtype: ListNode
    """

    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    # d = ListNode(4)

    a.next = b
    b.next = c
    # c.next = d

    print(reverseList(a))
