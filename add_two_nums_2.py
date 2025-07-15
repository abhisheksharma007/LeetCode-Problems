class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# l1 = [2,6,3]
# l2 = [5,6,4]
# out -[7,2,8]

# optimized solution
def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = 1 if total >= 10 else 0
            curr.next = ListNode(total % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next
    
def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, rem = divmod(total, 10)
            curr.next = ListNode(rem)
            curr = curr.next

        return dummy.next



# my solution
def addTwoNumbers(self, l1, l2):
        if not l1 or not l1:
            return None

        num1 = num2 = ''
        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next

        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next

        res = int(num1) + int(num2)
        res_list = [int(i) for i in str(res)]

        new_node = None
        i = len(res_list) - 1
        while i > -1:
            if not new_node:
                new_node = ListNode(res_list[i])
                new_head = new_node
            else:
                new_node.next = ListNode(res_list[i])
                new_node = new_node.next
            i -= 1

        return new_head
    
    
