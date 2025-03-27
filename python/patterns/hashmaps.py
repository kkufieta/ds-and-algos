def permutation_is_palindrome(s):
    d = {}
    odd_count = 0
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
        if d[ch]%2 == 1:
            odd_count += 1
        else:
            odd_count -= 1
    return odd_count <= 1