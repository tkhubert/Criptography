__author__ = 'tkhubert'

from CryptoImport import *

class CTR_AES:

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

        c_msg  = iv
        new_iv = int(hexlify(iv),16)
        for block in mBlocks:
            hx_iv = hex(new_iv)
            hx_iv = hx_iv[2:len(hx_iv)-1]
            c_msg = c_msg + strxor(block, self.cipher.encrypt(unhexlify(hx_iv)))
            new_iv = new_iv + 1
        return c_msg


    def decrypt(self, c_msg):
        iv      = self.getIV(c_msg)
        cBlocks = self.getMsgBlocks(c_msg)

        msg    = iv
        new_iv = int(hexlify(iv),16)
        for block in cBlocks:
            hx_iv = hex(new_iv)
            hx_iv = hx_iv[2:len(hx_iv)-1]
            msg = msg + strxor(block, self.cipher.encrypt(unhexlify(hx_iv)))
            new_iv = new_iv + 1
        return msg


def main():
    ivSize = 16

    k1 = "36f18357be4dbd77f050515c73fcf9f2"
    c1 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
    k2 = "36f18357be4dbd77f050515c73fcf9f2"
    c2 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"

    cipher1 = CTR_AES(unhexlify(k1), ivSize)
    cipher2 = CTR_AES(unhexlify(k2), ivSize)
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