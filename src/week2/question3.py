'''
Created on Feb 10, 2015

@author: xinghuangxu
'''

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.strxor import strxor


key='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
cipher = AES.new(key, AES.MODE_ECB)
iv='69dda8455c7dd4254bf353b773304eec'
print iv[:16]
# iv='4bf353b773304eec'
counter = int(iv[16:],16)

ctblocks=[
'0ec7702330098ce7f7520d1cbbb20fc3',
'88d1b0adb5054dbd7370849dbf0b88d3',
'93f252e764f1f5f7ad97ef79d59ce29f',
'5f51eeca32eabedd9afa932900000000'
]

ptblocks=[]

for x in range(0,len(ctblocks)):
    print iv[:16]+hex(counter)[2:]
    tempKey=(iv[:16]+hex(counter)[2:]).decode('hex')
    ct=ctblocks[x].decode('hex')
    pt= strxor(cipher.encrypt(tempKey),ct)
    ptblocks.append(pt)
    counter=counter+1

sum=""
for x in ptblocks:
    sum+= x
print sum

# plaintext= cipher.decrypt("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81");
# print plaintext
# msg = iv + cipher.encrypt(b'Attack at dawn')
# print msg.encode('hex')