# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(next=head)
        one = head
        two = one.next
        if two is None:
            return None

        three = two.next
        if three is None:
            return head.next


        while True:
            two.next = three.next
            three.next = two
            one.next = three

            one = two

            two = one.next
            if two is None:
                break

            three = two.next
            if three is None:
                break


        return head.next

        
