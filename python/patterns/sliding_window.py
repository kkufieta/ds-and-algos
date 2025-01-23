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