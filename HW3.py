__author__ = 'tkhubert'

from CryptoImport import *

BLOCK_SIZE = 1024

def main():
    files = ["6-2-GenericBirthdayAttack.mp4","6-1-Introduction.mp4"]
    res   = ["03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8","5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949"]

    i = 0
    for file in files:
        f = open(file,mode="rb")
        blocks = []
        block  = f.read(BLOCK_SIZE)
        while (block!=""):
            blocks.append(block)
            block = f.read(BLOCK_SIZE)

        n = len(blocks)
        currentHash = unhexlify("")
        for block in reversed(blocks):
            h = SHA256.new()
            h.update(block+currentHash)
            currentHash = h.digest()
        print hexlify(currentHash)
        print hexlify(currentHash)==res[i]
        i = i+1
        f.close()

if __name__=='__main__':
    main()