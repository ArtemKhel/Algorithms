
def boyer_moore(string, pattern):
    ls = len(string)
    lp = len(pattern)
        
    border = [0] * (lp + 1)
    shift = [0] * (lp + 1)
    
    bad_char = get_bad_char(pattern)
    get_strong_suffix(pattern, border, shift)
    get_partial_suffix(border, shift, lp)
    
    i = 0
    while i <= ls - lp:
        j = lp - 1
        while j >= 0 and pattern[j] == string[i + j]:
            j -= 1

        if j < 0:
            yield i
            i = i + shift[0]
        else:
            i = i + max(shift[j + 1], j - bad_char.get(string[i + j], lp))
    return -1


def get_bad_char(pattern):
    bad_char = {}
    for pos, char in enumerate(pattern[:-1]):
        bad_char[char] = pos
    return bad_char


def get_strong_suffix(pattern, border, shift):
    lp = len(pattern)
    
    i = lp
    j = lp + 1
    border[i] = j
    while i > 0:
        while j <= lp and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j
    return shift


def get_partial_suffix(border, shift, lp):
    j = border[0]
    for i in range(lp + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border[j]



string = 'GCAGCAGAGCAAGAGTATACAGGCAGATGCAGAGAG'
pattern = 'GCAGA'
print([i for i in boyer_moore(string, pattern)])

string =  'skakalka'
pattern = 'alk'
print([i for i in boyer_moore(string, pattern)])

string =  'olokolokol'
pattern = 'okol'
print([i for i in boyer_moore(string, pattern)])
        
string =  'aaaaa'
pattern = 'a'
print([i for i in boyer_moore(string, pattern)])

string =  'abcdef'
pattern = 'x'
print([i for i in boyer_moore(string, pattern)])


