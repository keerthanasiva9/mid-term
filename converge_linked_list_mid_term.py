#Q-1 : Write a function to determine whether two singly-linked lists are converging.

# Time complexity : o(x + y) where x and y are the size of linked list
# Space complexity : o(x) size of hashmap

class ListNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None

def are_converging(node1, node2):
    temp_map = set()
    while node1 is not None:
        temp_map.add(node1)
        node1 = node1.nxt

    while node2 is not None:
        if node2 in temp_map:
            return True
        node2 = node2.nxt

    return False

if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(5)
    l3 = ListNode(7)

    l1.nxt = l2
    l2.nxt = l3

    x1 = ListNode(2)
    x2 = ListNode(10)
    x1.nxt = x2
    x2.nxt = l2

    print(are_converging(l1, x1))

