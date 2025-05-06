from collections import defaultdict

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


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        count = [0]*26
        for l in w:
            count[ord(l)-ord('a')] += 1
        groups[tuple(count)].append(w)
    return list(groups.values())