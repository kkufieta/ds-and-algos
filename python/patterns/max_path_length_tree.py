def get_max_path_length_recursive(root):
    if not root:
        return 0

    # max path length
    m = 0
    _, m = get_m_recursive(root, m)

    return m


def get_m_recursive(node, m):
    le, ri = 0, 0
    if node.left:
        le, m = get_m_recursive(node.left, m)
    if node.right:
        ri, m = get_m_recursive(node.right, m)

    return max(le, ri) + 1, max(m, le + ri)


def get_max_path_length_sequential(root):
    if not root:
        return 0

    l_queue, le, ri, m = [], None, None, 0
    nodes = [root]
    while nodes:
        node = nodes[-1]
        if le is None:
            if node.left:
                nodes.append(node.left)
                if l_queue:
                    l_queue.append(None)
            else:
                le = 0
        elif ri is None:
            if node.right:
                nodes.append(node.right)
                l_queue.append(le)
                le = None
            else:
                ri = 0
        else:
            nodes.pop()
            local_max = max(le, ri) + 1
            m = max(m, le + ri)
            le, ri = None, None
            if not l_queue or l_queue[-1] is None:
                le = local_max
            else:
                le = l_queue[-1]
                ri = local_max
            if l_queue:
                l_queue.pop()

    return m
