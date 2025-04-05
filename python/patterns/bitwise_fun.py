def find_difference(str1, str2):
    r = 0
    for ch in str1 + str2:
        r ^= ord(ch)
    r = chr(r)
    return str1.find(r) if len(str1) > len(str2) else str2.find(r)

def swap_without_extra_space(x, y):
    x ^= y
    y ^= x
    x ^= y
    return x, y
