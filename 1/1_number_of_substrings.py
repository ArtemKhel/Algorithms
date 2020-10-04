

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


def count_substrings(string):
    cnt = 0
    len_ = len(string)
    for i in range(1, len_ + 1):
        cnt += i - max(prefix_function(string[len_ - i:len_]))
    return cnt


string = 'abcde'
print(count_substrings(string))
