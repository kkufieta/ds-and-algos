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

# Find repeated DNA sequences of size k (A, C, G, T)
def find_repeated_dna_sequence_size_k(s, k):
    if len(s) < k:
        return []
    code = {'A': 0, 'C': 1, 'G': 2, 'T': 3,
            0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    num = 0
    for i in range(k):
        num += code[s[i]] * 10**(k-1-i)
    d = {num: 1}
    result = []
    for i in range(k, len(s)):
        num = (num % 10**(k-1)) * 10 + code[s[i]]
        if num not in d:
            d[num] = 0
        elif d[num] == 1:
            result.append("".join([code[(num//10**(k-1-power))%10] for power in range(k)]))
        d[num] += 1

    return result

# Find repeated DNA sequences of size 10 (A, C, G, T)
def find_repeated_dna_sequence_size_10(s):
    return find_repeated_dna_sequence_size_k(s, 10)
