# repeated DNA sequences
def dna_sequences_naive(dna, k):
    seen = set()
    seen_twice = set()

    for i in range(len(dna) - k + 1):
        if dna[i:i+k] in seen:
            seen_twice.add(dna[i:i+k])
        else:
            seen.add(dna[i:i+k])
    return seen_twice

def rolling_hash_base_4(s):
    code = {'A': 0, 'C': 1, 'G': 2, 'T': 3,
            0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    num = 0
    for i, ch in enumerate(s):
        num += code[ch] * 4**(len(s)-1-i)
    return num


# Find repeated DNA sequences of size k (A, C, G, T)
def find_repeated_dna_sequence_size_k(s, k):
    if len(s) < k:
        return []
    code = {'A': 0, 'C': 1, 'G': 2, 'T': 3,
            0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    num = 0
    for i in range(k):
        num += code[s[i]] * 4**(k-1-i)
    d = {num: 1}
    result = []
    for i in range(len(s)-k):
        num = num * 4 - code[s[i]] * 4**(k) + code[s[i+k]]
        if num not in d:
            d[num] = 0
        elif d[num] == 1:
            result.append(s[i+1:i+k+1])
        d[num] += 1
    return result

# Find repeated DNA sequences of size 10 (A, C, G, T)
def find_repeated_dna_sequence_size_10(s):
    return find_repeated_dna_sequence_size_k(s, 10)
