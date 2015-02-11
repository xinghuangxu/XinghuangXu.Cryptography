'''
Created on Feb 11, 2015

@author: xinghuangxu
'''
import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
#             print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

    def replacebyte(self,ciphertext,index,guess):
        return ciphertext[:index*2-2]+ self.convertToHexStr(guess)+ciphertext[(index*2):]
    
    def convertToHexStr(self, hexNum):
        value=hex(hexNum)[2:]
        if hexNum<16:
            return '0'+value
        return value
    
    def getMessageWithIndex(self,ct,index):
        #first 16 bytes are iv
        nIndex=32*index
        vi=ct[nIndex:nIndex+32]
        data=ct[32:]
        output = self.crackMessage(vi,data[nIndex:nIndex+32])
        print "".join(output)
        return output
#         print 
#         print vi,
#         nIndex=32*index
#         print data[nIndex:nIndex+32]
    
    def crackMessage(self,iv,ct):
        result=[]
        charStr=[]
        for p in reversed(range (1,17)):
            xorNum=17-p
            print xorNum
            guess=0
            known=[]
            temp=iv
            for i in range(len(result)):
                known.append(self.convertToHexStr(result[i]^xorNum))
            suffix="".join(reversed(known));
            temp=temp[:len(temp)-len(suffix)]+suffix
            print temp
            for i in range(0,256):
                newIv=self.replacebyte(temp, p, guess^xorNum)
                if(self.query(newIv+ct)):
                    print newIv
                    print hex(guess)
                    result.append(guess)
                    charStr.append(chr(guess))
                    break
                guess=guess+1
        return reversed(charStr)
    
    def xor_strings(self,xs, ys):
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
        

if __name__ == "__main__":
    po = PaddingOracle()
    ct="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
#     po.query(ct)       # Issue HTTP query with the given argument
#     print po.replacebyte(ct, 2, 0xab)
#     po.convertToHexStr(98)
    result=""
    for x in range (0,1):   #0,3
        result=result+"".join(po.getMessageWithIndex(ct, x))

