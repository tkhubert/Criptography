__author__ = 'tkhubert'

from CryptoImport import *

def main():
    # HW4
    print "HW4------------------"
    y2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    print y2
    print y2.decode('hex')
    print unhexlify(y2)

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