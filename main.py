import traceback


def decrypt(string):
    res = list()
    for i in range(0, 26):
        res.append(0)
    for i in range(0, len(string)):
        if 97 <= ord(string[i]) <= 122:
            res[ord(string[i]) - 97] += 1
    return ''.join(str(e) for e in res)


try:
    assert decrypt('$aaaa#bbb*cc^fff!z') == '43200300000000000000000001'
    assert decrypt('jgsm3w#?7-5r#_jaaaaaqyk') == '50000010021010001110001010'
    assert decrypt('e$5e@*zd6f2vje3kauuu') == '10013100011000000000310001'
    assert decrypt('6!=b%g@&jnbb%=2h^fbs7') == '04000111010001000010000000'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
