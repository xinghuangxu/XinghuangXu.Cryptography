'''
Created on Feb 10, 2015

@author: xinghuangxu
'''

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.strxor import strxor

msg="Sixteen is bytes"
iv = Random.new().read(AES.block_size)
key='140b41b22a29beb4061bda66b6747e14'.decode('hex')
cipher = AES.new(key, AES.MODE_ECB)
iv='5b68629feb8606f9a6667670b75b38a5'.decode('hex')
ctblocks=[
'b4832d0f26e1ab7da33249de7d4afc48',
'e713ac646ace36e872ad5fb8a512428a',
'6e21364b0c374df45503473c5242a253',
]

ptblocks=[]
tempKey=iv
for x in range(0,len(ctblocks)):
    ct=ctblocks[x].decode('hex')
    pt= strxor(cipher.decrypt(ct),tempKey)
    ptblocks.append(pt)
    tempKey=ct

sum=""
for x in ptblocks:
    sum+= x
print sum

# plaintext= cipher.decrypt("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81");
# print plaintext
# msg = iv + cipher.encrypt(b'Attack at dawn')
# print msg.encode('hex')