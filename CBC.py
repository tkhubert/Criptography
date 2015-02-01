__author__ = 'tkhubert'

from CryptoImport import *

class CBC_AES:

    def __init__(self, key, sizeIV):
        self.sizeIV = sizeIV
        self.cipher = AES.new(key)

    def getIV(self, msg):
        return msg[0:self.sizeIV]

    def getMsgBlocks(self, msg):
        n        = len(msg)
        msgSize  = n - self.sizeIV
        nbBlocks = (msgSize-1)/AES.block_size+1

        mBlocks = []
        start = self.sizeIV
        for i in range(nbBlocks):
            if (start+AES.block_size<n):
                m = msg[start:start + AES.block_size]
            else:
                m = msg[start:n]

            mBlocks.append(m)
            start = start + AES.block_size

        return mBlocks

    def encrypt(self, msg):
        iv      = self.getIV(msg)
        mBlocks = self.getMsgBlocks(msg)

        c_msg = iv
        prev  = iv
        for block in mBlocks:
            prev = self.cipher.encrypt(strxor(block, prev))
            c_msg = c_msg + prev

        return c_msg

    def decrypt(self, c_msg):
        iv      = self.getIV(c_msg)
        cBlocks = self.getMsgBlocks(c_msg)

        msg   = iv
        prev  = iv
        for block in cBlocks:
            msg = msg + strxor(self.cipher.decrypt(block), prev)
            prev = block

        return msg

def main():
    ivSize = 16

    k1 = "140b41b22a29beb4061bda66b6747e14"
    c1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
    k2 = "140b41b22a29beb4061bda66b6747e14"
    c2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"

    cipher1 = CBC_AES(unhexlify(k1), ivSize)
    cipher2 = CBC_AES(unhexlify(k2), ivSize)
    m1 = cipher1.decrypt(unhexlify(c1))
    m2 = cipher2.decrypt(unhexlify(c2))

    print "msg1: " + str(m1[ivSize:])
    print "msg2: " + str(m2[ivSize:])

    c1b = cipher1.encrypt(m1)
    c2b = cipher2.encrypt(m2)
    print hexlify(c1b)==c1
    print hexlify(c2b)==c2

if __name__=='__main__':
    main()