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

# Find repeated DNA sequences of size 10 (A, C, G, T)
def find_repeated_dna_sequence_size_10(s):
    if len(s) < 10:
        return []
    code = {'A': 0, 'C': 1, 'G': 2, 'T': 3,
            0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    num = 0
    for i in range(10):
        num += code[s[i]] * 10**(9-i)
    d = {num: 1}
    result = []
    for i in range(10, len(s)):
        num = (num % 10**9) * 10 + code[s[i]]
        if num not in d:
            d[num] = 0
        elif d[num] == 1:
            result.append("".join([code[(num//10**(9-power))%10] for power in range(10)]))
        d[num] += 1

    return result

def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []
    enc = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    dec = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }
    num = 0
    for i in range(10):
        num += enc[s[i]] * 10**(9-i)
        
    result = []
    d = {num: 1}
    for i in range(10, len(s)):
        num = (num % (10 ** 9)) * 10 + enc[s[i]]
        if num not in d:
            d[num] = 0
        elif d[num] == 1:
            result.append("".join([dec[num//(10**(9-power))%10] for power in range(10)]))
        d[num] += 1
            
    return result
