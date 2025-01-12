def get_max_path_length_recursive(root):
    if not root:
        return 0

    # max path length
    m = 0
    _, m = get_m_recursive(root, m)

    return m

def get_m_recursive(node, m):
    l, r = 0, 0
    if node.left:
        l, m = get_m_recursive(node.left, m)
    if node.right:
        r, m = get_m_recursive(node.right, m)

    return max(l, r) + 1, max(m, l + r)


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
