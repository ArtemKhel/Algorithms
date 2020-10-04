

def prefix_function(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


def smallest_period(string):
    len_ = len(string)
    string = string * 2
    c= len_ - 1
    p = prefix_function(string)
    for i in range(len_, len_ * 2):
        if p[i] >= len_:
            c = i
            break
    
    return c - len_ + 1


string = 'abcdabcd'
print((smallest_period(string)))

