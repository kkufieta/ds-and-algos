def zigzaglines(s, k):
    if s == "" or k == 0:
        return ""
    if len(s) == 1 or k == 1:
        return s

    zz = ""    
    for i in range(min(len(s), k)):
        num_spaces_1 = (k - 2 - i) * 2 + 1
        num_spaces_2 = (i - 1) * 2 + 1
        if num_spaces_1 < 0:
            num_spaces_1 = num_spaces_2
        if num_spaces_2 < 0:
            num_spaces_2 = num_spaces_1


        zz += " " * i
        j = i
        while j < len(s):
            zz += s[j]
            j += num_spaces_1 + 1
            if j >= len(s):
                break
            zz += " " * num_spaces_1

            zz += s[j]
            j += num_spaces_2 + 1
            if j >= len(s):
                break
            zz += " " * num_spaces_2
        
        zz += "\n"


    return zz[:-1]