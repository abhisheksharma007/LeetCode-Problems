
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
def buildTree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    q = [root]
    i = 1
    while i < len(nums):
        curr = q.pop(0)
        if i < len(nums):
            curr.left = TreeNode(nums[i])
            q.append(curr.left)
            i += 1
        if i < len(nums):
            curr.right = TreeNode(nums[i])
            q.append(curr.right)
            i += 1
    return root
 
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)
    
# nums = [1, 2, 3, 4, 5, 6, 6, 6, 6]
nums = [4,2,7,1,3,6,9]
# nums = [2,1,3]
# nums = [1,2,3,4,None,None,5]
root = buildTree(nums)

def invert_bin_tree(nums):
    if not nums:
        return
    invert_bin_tree(nums.left)
    invert_bin_tree(nums.right)
    nums.left, nums.right = nums.right, nums.left
    return None

invert_bin_tree(root)

printTree(root)































