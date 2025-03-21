def valid_palindrome(s):
    s = s.lower()
    p_left, p_right = 0, len(s)-1
    while p_left < p_right:
        if s[p_left] != s[p_right]:
            return False
        p_left += 1
        p_right -= 1
    return True