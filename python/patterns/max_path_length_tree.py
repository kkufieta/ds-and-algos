from lib import tree
def get_max_path_length_recursive(root):
    if not root:
        return 0
    return get_m_recursive(root)[1]


def get_m_recursive(node):
    l, r, m_l, m_r = 0, 0, 0, 0
    if node.left:
        l, m_l = get_m_recursive(node.left)
        l += 1
    if node.right:
        r, m_r = get_m_recursive(node.right)
        r += 1

    return max(l, r), max(m_l, m_r, l + r)

def diameter_of_tree(root):
    if not root:
        return 0
    return get_max_length(root)[1]

def get_max_length(node):
    def get_length(node):
        if node:
            length, max_length = get_max_length(node)
            return length + 1, max_length
        return 0, 0
    len_l, max_len_l = get_length(node.left)
    len_r, max_len_r = get_length(node.right)
    return max(len_l, len_r), max(max_len_l, max_len_r, len_l + len_r)


def get_max_path_length_sequential(root):
    if not root:
        return 0

    l_queue, l, r, m = [], None, None, 0
    nodes = [root]
    while nodes:
        node = nodes[-1]
        if l == None:
            if node.left:
                nodes.append(node.left)
                if l_queue:
                    l_queue.append(None)
            else:
                l = 0
        elif r == None:
            if node.right:
                nodes.append(node.right)
                l_queue.append(l)
                l = None
            else:
                r = 0
        else:
            nodes.pop()
            local_max = max(l, r) + 1
            m = max(m, l + r)
            l, r = None, None
            if not l_queue or l_queue[-1] == None:
                l = local_max
            else:
                l = l_queue[-1]
                r = local_max
            if l_queue:
                l_queue.pop()

    return m
