from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"Listnode({self.val, self.next})"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_no = ""
        l2_no = ""
        while True:
            try:
                if l1.val or l1.val == 0:
                    l1_no += str(l1.val)
                    l1 = l1.next
            except AttributeError:
                pass
            try:
                if l2.val or l2.val == 0:
                    l2_no += str(l2.val)
                    l2 = l2.next
            except AttributeError:
                pass
            try:
                if not l1.val:
                    pass
            except AttributeError:
                try:
                    if not l2.val:
                        pass
                except AttributeError:
                    break
        l1_no = int(str(l1_no)[::-1])
        l2_no = int(str(l2_no)[::-1])
        new_no = str(l1_no + l2_no)[::-1]
        l3 = ListNode(int(new_no[-1]))

        for num in range(len(str(new_no))-2, -1, -1):
            l3 = ListNode(int(str(new_no)[num]), l3)
            
        return l3 


sol = Solution()
l1 = ListNode(5, ListNode(6))
l2 = ListNode(5, ListNode(4, ListNode(9)))
print(sol.addTwoNumbers(l1, l2))