'''
Created on Feb 10, 2015

@author: xinghuangxu
'''
from hashlib import sha256

def readChunk(fileObj, chunkSize=1024):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 1kB.
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


fileHandler=open(r"test1.mp4","rb")

blocks=[]
for chunk in readChunk(fileHandler):
    blocks.append(chunk)

suffix=b''
for i in reversed(blocks):
    block= i + suffix
    suffix=sha256(block).digest()

print suffix.encode('hex')
