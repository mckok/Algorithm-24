class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def preorder(n) :
    if n is not None :
        print(n.data, end='  ')
        preorder(n.left)
        preorder(n.right)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end='  ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end='  ')
        
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('f', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)
print('  In-order : ', end='')
inorder(root)
print()
print('  Pre_Order : ', end='')
preorder(root)
print()
print('  Post_Order : ', end='')
postorder(root)
print()