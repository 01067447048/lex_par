# coding:utf-8
import hashlib
import time
from revfsdsfawg3 import REvfsdsfawg3
from rpc import BroadCast

class vwsferWRER24134d(REvfsdsfawg3):

    def __init__(self, xcvsdf235sdfg234q13, vv3xwvwt32, tx, x34vx34xf34):
        self.index = xcvsdf235sdfg234q13
        self.timestamp = vv3xwvwt32
        self.tx = tx
        self.previous_block = x34vx34xf34

    def dfnes(self):
        """
        Refer to bitcoin block header hash
        """          
        return hashlib.sha256((str(self.index) + str(self.timestamp) + str(self.tx) + str(self.previous_block)).encode('utf-8')).hexdigest()

    def snrfgh(self):
        """
        Proof of work. Add nouce to block.
        """        
        nouce = 0
        while self.anertw(nouce) is False:
            nouce += 1
        self.nouce = nouce
        return nouce

    def abg(self, nouce):
        """
        Block hash generate. Add hash to block.
        """
        self.hash = self.ghash(nouce)
    
    def ghash(self, nouce):
        """
        Block hash generate.
        """        
        header_hash = self.dfnes()
        token = ''.join((header_hash, str(nouce))).encode('utf-8')
        return hashlib.sha256(token).hexdigest()

    def anertw(self, nouce):
        """
        Validates the Proof
        """
        return self.ghash(nouce)[:4] == "0000"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def dfahwe3(cls, mdfwre):
        b = cls(mdfwre['index'], mdfwre['timestamp'], mdfwre['tx'], mdfwre['previous_block'])
        b.hash = mdfwre['hash']
        b.nouce = mdfwre['nouce']
        return b

    @staticmethod
    def adfghew234(block):
        BroadCast().new_block(block)