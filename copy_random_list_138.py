class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
        
        
# my solution
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        new_head = None
        
        idx_og = {}
        idx_nn = {}
        idx_rdm = {}
        i = 0

        # create copy from old list without random pointers
        while curr:
            new_node = Node(curr.val)
            if not new_head:
                new_head = new_node
            
            if i > 0:
                idx_nn[i-1].next = new_node

            idx_og[curr] = i
            idx_nn[i] = new_node

            curr = curr.next
            i += 1

        curr = head
        i = 0
        while curr:
            idx_rdm[i] = idx_og.get(curr.random, None)
            curr = curr.next
            i += 1

        new = new_head
        i = 0
        while new:
            if idx_rdm.get(i) is not None:
                new.random = idx_nn[idx_rdm[i]]
            new = new.next
            i += 1
        return new_head        
        


# Explaination

# eg. 
# A(C) -> B(A) -> C(NA) -> D(B) -> NA

# 1. 
# A -> a(A, B) -> B -> b(B, C) -> C -> c(C, D) -> D -> d(D, NA) -> NA

# 2. 
# A -> a(A, B)(c(C, D)) -> B -> b(B, C)(a(A, B)) -> C -> c(C, D)() -> D -> d(D, NA)(b(B, C)) -> NA

# 3. 
# new_head: a(A, B)(c(C, D))

# curr: A -> B -> C -> D -> NA

# copy: a(A, B)(c(C, D)) -> b(B, C)(a(A, B)) -> c(C, D)() -> d(D, NA)(b(B, C)) -> NA

# out: a(c) -> b(a) -> c(na) -> d(b) -> NA


# space optimized solution -> three pass solution
def copyRandomList(head):
    if not head:
        return None

    # 1. Interleave copied nodes with original nodes
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next

    # 2. Assign random pointers for the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # 3. Separate the copied list from the original list
    curr = head
    new_head = head.next
    while curr:
        copy = curr.next
        curr.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        curr = curr.next

    return new_head
