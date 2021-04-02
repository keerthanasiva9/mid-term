#Q-2 : Print perimeter of a tree(in clock-wise order).
#Example : Expected output for the following tree should be : [1,3,7,14,13,11,10,9,8,4,2]

# Space complexity : O(n) as we use a stack here
# Time complexity : O(n) as we traverse the whole tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False

    def if_leaf(self,node):
        if node.left is None and node.right is None:
            return True
        return False

def print_child(node):
    if node.visited is False and node.if_leaf(node):
        print(node.data)
        node.visited = True
    if node.right:
        print_child(node.right)
    if node.left:
        print_child(node.left)

stack = []

def print_left_boundry(root):
    if root.visited is False:
        stack.append(root.data)
        root.visited = True
    if root.left:
        print_left_boundry(root.left)

def print_right_boundry(root):
    if root.visited is False:
        print(root.data)
        root.visited = True
    if root.right:
       print_right_boundry(root.right)
    if root.left:
        print_right_boundry(root.left)

def print_clock_wise_perimeter(root):

    if (root):
        print(root.data)
        root.visited = True
        if root.right:
            print_right_boundry(root.right)
        print_child(root)
        if root.left:
            print_left_boundry(root.left)
        while len(stack) != 0:
            print(stack.pop())


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.left.right = Node(6)
    root.left.right.right = Node(5)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.left = Node(4)
    print_clock_wise_perimeter(root)

