__author__ = 'tkhubert'

from CryptoImport import *

cipherhex = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
BLOCK_SIZE = 16

chars = '9 etaonihsrdluwmcygf,pb.vk"I\'-T;HMAWS_B?xjE!LCDqzYNPOJGR:FUKV*)(0XQ2/3854671]$Z[@&#%+<=>\\^`{|}~'

def decrypt(c1):
    po = PaddingOracle()

    guess = ""
    table = ""
    for i in reversed(range(BLOCK_SIZE)):
        idx = BLOCK_SIZE - i

        null = '\x00'*i
        pad =  null + idx * chr(idx)

        found = False
        for c in range(256):#32,127):
            newIv = null + chr(c) + guess
            newIv = strxor(newIv, pad)

            q = po.query(hexlify(newIv+c1))
            if (q or q==None):
                guess = chr(c) + guess
                found = True
                break

        if found:
            print idx, guess
        else:
            print idx, "error"
    return guess

def main():
    cipher   = unhexlify(cipherhex)
    size     = len(cipher)

    blocks = []
    for i in range(size/BLOCK_SIZE):
        blocks.append(cipher[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE])

    guess = ""
    for i in reversed(range(1,size/BLOCK_SIZE)):
        g = decrypt(blocks[i])
        guess = strxor(g, blocks[i-1]) + guess
        print guess



if __name__ == "__main__":
    main()