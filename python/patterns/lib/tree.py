import queue

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def create_from_list(self, bt_list):
        if not bt_list or not bt_list[0]:
            return

        q = queue.Queue()
        i = 0
        self.root = BinaryTreeNode(bt_list[i])
        q.put(self.root)
        while i < len(bt_list):
            if q.qsize() == 0:
                return
            node = q.get()
            i += 1
            if i < len(bt_list) and bt_list[i]:
                node.left = BinaryTreeNode(bt_list[i])
                q.put(node.left)
            i += 1
            if i < len(bt_list) and bt_list[i]:
                node.right = BinaryTreeNode(bt_list[i])
                q.put(node.right)


    def to_list(self):
        bt_list = []
        if not self.root:
            return bt_list

        node_queue = queue.Queue()
        node_queue.put(self.root)
        none_count = 0
        while not node_queue.empty():
            node = node_queue.get()
            if not node:
                none_count += 1
            else:
                bt_list = bt_list + [None] * none_count
                none_count = 0
                bt_list.append(node.data)
                node_queue.put(node.left)
                node_queue.put(node.right)

        return bt_list
        
