

def z_function(text):
    l = r = 0
    z = [0 for i in range(len(text))]

    for i in range(1, len(text) - 1):
        if i < r:
            z[i] = min(r - i + 1, z[i-l])
        while i + z[i] < len(text) and text[z[i]] == text[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = l + z[i] - 1
    
    return z


def fuzzy_search(text, string):
    ls, lt = len(string), len(text)
    l_to_r = z_function(string + text)[ls:]
    r_to_l = z_function(string[::-1] + text[::-1])[ls:]

    for i in range(0, lt - ls + 1):

        if l_to_r[i] == ls:
            print(f'Full match at {i}: {text[max(0, i-5):min(i + ls + 5, lt)]}')

        elif (len(string) > 1) and (l_to_r[i] + r_to_l[lt - ls - i] == ls - 1):
            print(f'Partial match at {i}: {text[max(0, i-5):min(i + ls + 5, lt)]}')

        elif (len(string) > 1) and (l_to_r[i] + r_to_l[lt - ls - i + 1] == ls - 1):
            print(f'Partial match at {i}: {text[max(0, i-5):min(i + ls + 4, lt)]}')


text = 'TEST_abcdefgh_TECT_ijklmnop_TST_qrstuvwxyz_TEST'
string = 'TEST'

fuzzy_search(text, string)

