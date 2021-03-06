__author__ = 'tkhubert'

from CryptoImport import *
from CBC import CBC_AES

def main():
    # HW5
    print "HW5------------------"

    # HW4
    print "HW4------------------"
    iv  = '20814804c1767293b99f1d9cab3bc3e7'
    key = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    msg = 'Pay Bob 100$    '
    iv1 = '        500$    '
    iv2 = '        100$    '

    cipher = AES.new(unhexlify(key), AES.MODE_CBC, unhexlify(iv))
    c = unhexlify(iv)+cipher.encrypt(msg)
    d = cipher.decrypt(c)
    c1 = strxor(strxor(unhexlify(iv), iv1), iv2) + c[16:]
    d1 = cipher.decrypt(c1)
    print hexlify(c)
    print hexlify(c1)
    print d[16:]
    print d1[16:]

    c  = '20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d'
    c  = unhexlify(c)
    iv = c[:16]
    c1 = strxor(strxor(iv, iv1), iv2) + c[16:]
    print hexlify(c)
    print hexlify(c1)
    d1 = cipher.decrypt(c1)
    print d1[16:]

    # HW3
    print "HW3------------------"
    y2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    x2 = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    c2 = "f2fdac83238d6d32e4f6da0930d58216"
    d2 = hexxor(c2, y2)
    print d2
    d2 = "585706298927c7984e5c70a39a7f28bc"
    y1 = "00000000000000000000000000000000"
    x1 = "219c8cb0fe96e8de9c4f7cc8c48f954a"

    x4 = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    y4 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    c4 = "ff5afe64213e5e63f6042b1dc08d27f6"
    d4 = hexxor(c4, y4)
    x3 = "00000000000000000000000000000000"
    c3 = "66e94bd4ef8a2c3b884cfa59ca342b2e"
    y4 = hexxor(d4, c3)
    print y4
    y4 = "33191f1a641ed8f2d4e27beea013a672"


    # HW2
    print "HW2------------------"
    zero = "0000000000000000"
    one  = "FFFFFFFF00000000"
    c00 = "e86d2de2e1387ae9"
    c10 = "1792d21db645c008"

    print hexxor(zero, c00)
    print hexxor(one , c10)

    s0 = 'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
    s1 = 'An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.'
    s2 = 'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.'
    s3 = 'We see immediately that one needs little information to begin to break down the process.'
    print len(s0)
    print len(s1)
    print len(s2)
    print len(s2)
    print len(s3)

if __name__=='__main__':
    main()