def find_difference(str1, str2):
    r = 0
    for ch in str1 + str2:
        r = r ^ ord(ch)

    return str1.find(chr(r)) if len(str1) > len(str2) else str2.find(chr(r))

def swap_without_extra_space(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y