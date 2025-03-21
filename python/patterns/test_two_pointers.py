import pytest
from two_pointers import *

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