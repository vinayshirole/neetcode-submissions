# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = checker = head
        prev = None
        number_of_nodes = 0
        while checker:
            number_of_nodes += 1
            checker = checker.next

        counter = number_of_nodes - n

        if counter == 0:
            return head.next

        while curr:
            if counter == 0:
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            counter -= 1
        
        return head