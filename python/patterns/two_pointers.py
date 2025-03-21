def valid_palindrome(s):
    s = s.lower()
    p_left, p_right = 0, len(s)-1
    while p_left < p_right:
        if s[p_left] != s[p_right]:
            return False
        p_left += 1
        p_right -= 1
    return True

def reverse_string_in_place(s):
    p_left, p_right = 0, len(s)-1
    while p_left < p_right:
        s = s[0:p_left] + s[p_right] + s[p_left+1:p_right] + s[p_left] + s[p_right+1:]

        p_left += 1
        p_right -= 1
    return s