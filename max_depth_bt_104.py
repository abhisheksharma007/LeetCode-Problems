class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def maxDepth(root):
    if not root:
        return 0

    def _maxDepth(root, height=0):
        if not root:
            return height
        left_depth = _maxDepth(root.left, height+1)
        right_depth = _maxDepth(root.right, height+1)
        
        return max(left_depth, right_depth)
    
    return _maxDepth(root)

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def maxDepth(root):
    if not root:
        return 0
    queue = deque([root])
    level = 1
    while queue:
        for i in range(len(queue)): # remove all node from that level then increment the level
            nxt_node = queue.popleft()
            if nxt_node.left:
                queue.append(nxt_node.left)
            if nxt_node.right:
                queue.append(nxt_node.right)
        level += 1
    
    return level

# Test Cases
def create_tree_from_list(values, index=0):
    """Helper function to create a binary tree from a list representation"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree_from_list(values, 2 * index + 1)
    root.right = create_tree_from_list(values, 2 * index + 2)
    
    return root


# Test Case 1: Empty tree
print("Test Case 1: Empty tree")
print(f"Expected: 0, Got: {maxDepth(None)}")
print()

# Test Case 2: Single node tree
print("Test Case 2: Single node tree")
root1 = TreeNode(1)
print(f"Expected: 1, Got: {maxDepth(root1)}")
print()

# Test Case 3: Simple tree with 2 levels
print("Test Case 3: Simple tree with 2 levels")
#     1
#    / \
#   2   3
root2 = create_tree_from_list([1, 2, 3])
print(f"Expected: 2, Got: {maxDepth(root2)}")
print()

# Test Case 4: Tree with 3 levels
print("Test Case 4: Tree with 3 levels")
#       1
#      / \
#     2   3
#    / \
#   4   5
root3 = create_tree_from_list([1, 2, 3, 4, 5, None, None])
print(f"Expected: 3, Got: {maxDepth(root3)}")
print()

# Test Case 5: Unbalanced tree (left heavy)
print("Test Case 5: Unbalanced tree (left heavy)")
#     1
#    /
#   2
#  /
# 3
root4 = create_tree_from_list([1, 2, None, 3])
print(f"Expected: 3, Got: {maxDepth(root4)}")
print()

# Test Case 6: Unbalanced tree (right heavy)
print("Test Case 6: Unbalanced tree (right heavy)")
#     1
#      \
#       2
#        \
#         3
root5 = create_tree_from_list([1, None, 2, None, None, None, 3])
print(f"Expected: 3, Got: {maxDepth(root5)}")
print()

# Test Case 7: Complex tree
print("Test Case 7: Complex tree")
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#  /
# 7
root6 = create_tree_from_list([1, 2, 3, 4, 5, None, 6, 7])
print(f"Expected: 4, Got: {maxDepth(root6)}")
print()

# Test Case 8: Tree with only left children
print("Test Case 8: Tree with only left children")
#     1
#    /
#   2
#  /
# 3
#/
#4
root7 = create_tree_from_list([1, 2, None, 3, None, None, None, 4])
print(f"Expected: 4, Got: {maxDepth(root7)}")
print()

# Test Case 9: Tree with only right children
print("Test Case 9: Tree with only right children")
#     1
#      \
#       2
#        \
#         3
#          \
#           4
root8 = create_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
print(f"Expected: 4, Got: {maxDepth(root8)}")
print()

# Test Case 10: Large balanced tree
print("Test Case 10: Large balanced tree")
# This creates a tree with 4 levels
root9 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(f"Expected: 4, Got: {maxDepth(root9)}")
print()