head = [1,2,3,4,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(self, head):
    
    if not head:
        return None

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first = head
    second = slow.next
    
    prev = None
    slow.next = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    second = prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2




