class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, new_value) -> BinaryTreeNode:
    if root == None:
        root = BinaryTreeNode(new_value)
    elif new_value < root.data:
        root.left = insert(root.left, new_value)
    else: #new_value >= root.data:
        root.right = insert(root.right, new_value)
    return root        


def inorder(root) -> None:
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)


def preorder(root) -> None:
    if root:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)


def postorder(root) -> None:
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
