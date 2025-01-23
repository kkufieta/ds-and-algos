import pytest
from sliding_window import *


@pytest.mark.parametrize("dna, k, repeated_sequences", [
    ("GAGTCACAGTAGTTTCA", 3, ["AGT", "TCA"]),
    ("CAAACCCCGTAAACCCCA", 7, ["AAACCCC"]),
    ("AGCTGAAAGCTTAGCTG", 5, ["AGCTG"]),
    ("AGAGCTCCAGAGCTTG", 6, ["AGAGCT"]),
    ("ATATATATATATATAT", 6, ["TATATA", "ATATAT"]),
    ("AAAAACCCCCAAAAACCCCCC" , 8, ["AAAACCCC","AAACCCCC","AAAAACCC"]),
    ("GGGGGGGGGGGGGGGGGGGGGGGGG" , 9, ["GGGGGGGGG"]),
    ("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT" , 10, ["TTTTCCCCCC","TTCCCCCCCT","CCCCCCCTTT","TCCCCCCCTT","CCCCCTTTTT","CCCCTTTTTT","TTTCCCCCCC","TTTTTCCCCC","CCCCCCTTTT"]),
    ("AAAAAACCCCCCCAAAAAAAACCCCCCCTG" , 10, ["AAAAAACCCC","AAAAACCCCC","AAACCCCCCC","AAAACCCCCC"]),
    ("ATATATATATATATAT" , 6, ["TATATA","ATATAT"]),
])

def test_dna_sequences_naive(dna, k, repeated_sequences):
    output = list(dna_sequences_naive(dna, k))
    output.sort()
    repeated_sequences.sort()

    assert output == repeated_sequences