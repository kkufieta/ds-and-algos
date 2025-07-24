def get_max_path_length_recursive(root):
    if not root:
        return 0

    # max path length
    m = 0
    _, m = get_m_recursive(root, m)

    return m


def get_m_recursive(node, m):
    left, right = 0, 0
    if node.left:
        left, m = get_m_recursive(node.left, m)
    if node.right:
        right, m = get_m_recursive(node.right, m)

    return max(left, right) + 1, max(m, left + right)


def get_max_path_length_sequential(root):
    if not root:
        return 0

    l_queue, left, right, m = [], None, None, 0
    nodes = [root]
    while nodes:
        node = nodes[-1]
        if left is None:
            if node.left:
                nodes.append(node.left)
                if l_queue:
                    l_queue.append(None)
            else:
                left = 0
        elif right is None:
            if node.right:
                nodes.append(node.right)
                l_queue.append(left)
                left = None
            else:
                right = 0
        else:
            nodes.pop()
            local_max = max(left, right) + 1
            m = max(m, left + right)
            left, right = None, None
            if not l_queue or l_queue[-1] is None:
                left = local_max
            else:
                left = l_queue[-1]
                right = local_max

            if l_queue:
                l_queue.pop()
    return m
