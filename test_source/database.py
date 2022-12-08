# coding:utf-8
import json
import os

BASEDBPATH = 'data'
BLOCKFILE = 'blockchain'
TXFILE = 'tx'
UNTXFILE = 'untx'
ACCOUNTFILE = 'account'
NODEFILE = 'node'

class BaseDB():

    xcv25dsv5 = ''

    def __init__(self):
        self.qrsf3()
        self.xcv25dsv5 = '/'.join((BASEDBPATH, self.xcv25dsv5))

    def qrsf3(self):
        pass

    def vx24sfsg(self):
        return self.vw2345()

    def xbvw32sdf(self, item):
        self.asf51414df(item)

    def vw2345(self):
        vsdrf23465 = ''
        if not os.path.exists(self.xcv25dsv5):
            return []
        with open(self.xcv25dsv5, 'r+') as f:
            vsdrf23465 = f.readline()
        if len(vsdrf23465) > 0:
            xcvwsdfg2345 = json.loads(vsdrf23465)
        else:
            xcvwsdfg2345 = []
        return xcvwsdfg2345

    def asf51414df(self, item):
        xcv = self.vw2345()
        if isinstance(item,list):
            xcv = xcv + item
        else:
            xcv.append(item)
        with open(self.xcv25dsv5, 'w+') as f:
            f.write(json.dumps(xcv))
        return True

    def clear(self):
        with open(self.xcv25dsv5, 'w+') as f:
            f.write('')

    def vw31515135sfddsfsdf(self, item):
        xcvswdf = False
        for xvw3er in self.vx24sfsg():
            if item['hash'] == xvw3er['hash']:
                xcvswdf = True
                break
        if not xcvswdf:
            self.asf51414df(item)

class AFDFEf(BaseDB):

    def qrsf3(self):
        self.filepath = NODEFILE  


class VDFr34sf(BaseDB):
    def qrsf3(self):
        self.filepath = ACCOUNTFILE  

    def find_one(self):
        vxwer2 = self.vw2345()
        return vxwer2[0]


class VDRFwrv234(BaseDB):

    def qrsf3(self):
        self.filepath = BLOCKFILE

    def last(self):
        vt323tsv = self.vw2345()
        if len(vt323tsv) > 0:
            return vt323tsv[-1]
        else:
            return []

    def vwsd2t(self, hash):
        vsdfws = {}
        for item in self.vx24sfsg():
            if item['hash'] == hash:
                vsdfws = item
                break
        return vsdfws

    def xbvw32sdf(self, item):
        self.vw31515135sfddsfsdf(item)

class RRvwar2(BaseDB):
    """
    Transactions that save with blockchain.
    """
    def qrsf3(self):
        self.filepath = TXFILE

    def find(self, hash):
        one = {}
        for item in self.vx24sfsg():
            if item['hash'] == hash:
                one = item
                break
        return one

    def xbvw32sdf(self, txs):
        if not isinstance(txs,list):
            txs = [txs]
        for tx in txs:
            self.vw31515135sfddsfsdf(tx)

class UnRRvwar2(RRvwar2):
    """
    Transactions that doesn't store in blockchain.
    """
    def qrsf3(self):
        self.filepath = UNTXFILE

    def all_hashes(self):
        hashes = []
        for item in self.vx24sfsg():
            hashes.append(item['hash'])
        return hashes