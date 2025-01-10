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

    return 0