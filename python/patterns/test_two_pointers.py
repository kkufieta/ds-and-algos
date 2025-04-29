import pytest
from two_pointers import *

@pytest.mark.parametrize("nums, expected", [
    ([1,2,0,3,0,6,3,0,0,2], [1,2,3,6,3,2,0,0,0,0]),
    ([1,0,2,3,0,6,0,3,0,2], [1,2,3,6,3,2,0,0,0,0]),
    ([], []),
    ([0], [0]),
    ([1], [1]),
    ([1, 0], [1, 0]),
    ([0, 1], [1, 0]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),  # All zeros
    ([1, 2, 3, 4], [1, 2, 3, 4]),  # No zeros
    ([0, 0, 1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0, 0, 0]),  # Zeros interspersed
    ([0, 0, 0, 1], [1, 0, 0, 0]),  # Zeros followed by a single number
    ([1, 0, 0, 0], [1, 0, 0, 0]),  # Single number followed by zeros
    ([1, 0, 2, 0, 3, 0, 4, 0], [1, 2, 3, 4, 0, 0, 0, 0]),  # Alternating zeros and numbers
    ([0, 1, 0, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0, 0]),  # Alternating zeros and numbers starting with zero
    ([1, 0, 0, 2, 0, 0, 3, 0, 0, 4], [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]),  # Multiple zeros between numbers
    ([1, 2, 3, 0, 0, 0, 0], [1, 2, 3, 0, 0, 0, 0]),  # Zeros only at the end
    ([0, 0, 0, 0, 1, 2, 3], [1, 2, 3, 0, 0, 0, 0]),  # Zeros only at the beginning
    ([0, 1, 0, 0, 2, 0, 0, 3, 0, 0], [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]),  # Zeros interspersed with multiple gaps
    ([1, 0, 0, 0, 0, 0, 0, 0, 0, 2], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]),  # Large gap of zeros between numbers
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),  # All zeros in a large array
    ([1, 0, 2, 0, 3, 0, 4, 0, 5, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]),  # Alternating zeros and numbers with increasing sequence
    ([0, 5, 0, 4, 0, 3, 0, 2, 0, 1], [5, 4, 3, 2, 1, 0, 0, 0, 0, 0]),  # Alternating zeros and numbers with decreasing sequence
])
def test_move_zeros_back(nums, expected):
    assert move_zeroes_back(nums) == expected

@pytest.mark.parametrize("nums, sum_num, expected", [
    ([1, 2], 3, (0, 1)),
    ([1], 2, None),
    ([], 10, None),
    ([2, 2, 2], 4, (0, 2)),
    ([1, 3, 5, 7], 8, (0, 3)),  # Pair exists at the ends
    ([1, 3, 5, 7], 10, (1, 3)),  # Pair exists in the middle
    ([1, 3, 5, 7], 12, (2, 3)),  # Pair exists at the end of the array
    ([1, 2, 3, 4, 5], 9, (3, 4)),  # Pair exists at the end
    ([1, 2, 3, 4, 5], 1, None),  # Sum is less than the smallest element
    ([1, 2, 3, 4, 5], 10, None),  # Sum is greater than the largest possible pair
    ([0, 0, 0, 0], 0, (0, 3)),  # Multiple zeros
    ([-1, 0, 1, 2], 1, (0, 3)),  # Negative and positive numbers
    ([-5, -3, -1, 0, 2, 4], -4, (1, 2)),  # Negative numbers
    ([1, 1, 1, 1], 2, (0, 3)),  # Repeated elements
    ([1, 2, 3, 4, 4, 5], 8, (2, 5)),  # Duplicate numbers with valid pair
    ([1, 2, 3, 4, 5], 7, (1, 4)),  # Pair exists with non-adjacent elements
    ([1, 2, 3, 4, 5], 6, (0, 4)),  # Pair exists with adjacent elements
    ([10, 20, 30, 40, 50], 90, (3, 4)),  # Large numbers
    ([1, 2, 3, 4, 5], 0, None),  # Sum is zero, no valid pair
    ([1, 2, 3, 4, 5], -1, None),  # Negative sum, no valid pair
    ([1, 2, 3, 4, 5], 3, (0, 1)),  # Pair exists at the start
    ([1, 2, 3, 4, 5], 4, (0, 2)),  # Pair exists with gap
    ([1, 2, 3, 4, 5], 5, (0, 3)),  # Pair exists with larger gap
    ([1, 2, 3, 4, 5], 11, None),  # Sum exceeds all possible pairs
    ([1, 2, 3, 4, 5], 2, None),  # Sum equals a single element, no pair
])
def test_pair_with_sum(nums, sum_num, expected):
    assert pair_with_sum(nums, sum_num) == expected

@pytest.mark.parametrize("s, expected", [
    ("aba", True),
    ("abab", False),
    ("RACEACAR", False),
    ("RACECAR", True),
    ("kaYak", True),
    ("hello", False),
    ("RaCEACAR", False),
    ("A", True),
    ("ABCDABCD", False),
    ("", True),  # Empty string is a palindrome
    ("a", True),  # Single character is a palindrome
    ("aa", True),  # Two identical characters
    ("ab", False),  # Two different characters
    ("Able was I ere I saw Elba", True),  # Palindrome with spaces and mixed case
    ("No lemon, no melon", False),  # Palindrome with spaces and punctuation
    ("12321", True),  # Numeric palindrome
    ("12345", False),  # Non-palindromic numeric string
    ("Was it a car or a cat I saw", False),  # Complex palindrome with spaces
    ("Madam, in Eden, I'm Adam", False),  # Palindrome with punctuation
    ("Not a palindrome", False),  # Clearly not a palindrome
])
def test_valid_palindrome(s, expected):
    assert valid_palindrome(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("aba", "aba"),
    ("abab", "baba"),
    ("RACEACAR", "RACAECAR"),
    ("RACECAR", "RACECAR"),
    ("kaYak", "kaYak"),
    ("hello", "olleh"),
    ("RaCEACAR", "RACAECaR"),
    ("A", "A"),
    ("ABCDABCD", "DCBADCBA"),
    ("", ""),  # Empty string
    ("a", "a"),  # Single character
    ("aa", "aa"),  # Two identical characters
    ("ab", "ba"),  # Two different characters
    ("Able was I ere I saw Elba", "ablE was I ere I saw elbA"),  # Mixed case with spaces
    ("No lemon, no melon", "nolem on ,nomel oN"),  # Spaces and punctuation
    ("12321", "12321"),  # Numeric palindrome
    ("12345", "54321"),  # Numeric string
    ("Was it a car or a cat I saw", "was I tac a ro rac a ti saW"),  # Complex with spaces
    ("Madam, in Eden, I'm Adam", "madA m'I ,nedE ni ,madaM"),  # Punctuation
    ("Not a palindrome", "emordnilap a toN"),  # Non-palindromic string
    ("Python", "nohtyP"),  # Regular string
    ("racecar", "racecar"),  # Lowercase palindrome
    ("Palindrome", "emordnilaP"),  # Mixed case
    ("!@#$%^&*()", ")(*&^%$#@!"),  # Special characters
    ("123abcABC", "CBAcba321"),  # Alphanumeric string
])
def test_reverse_string_in_place(s, expected):
    assert reverse_string_in_place(s) == expected