# coding:utf-8
import time
import json
import hashlib
from revfsdsfawg3 import REvfsdsfawg3
from database import RRvwar2, UnRRvwar2
from rpc import BroadCast

class VVSF35wg(REvfsdsfawg3):
    def __init__(self, utxo_hash, amount):
        self.hash = utxo_hash
        self.amount = amount
        # self.unLockSig = unLockSig

class Vswdrq(REvfsdsfawg3):
    def __init__(self, receiver, amount):
        self.receiver = receiver
        self.amount = amount
        self.hash = hashlib.sha256((str(time.time()) + str(self.receiver) + str(self.amount)).encode('utf-8')).hexdigest()
        # self.lockSig = lockSig
    
    @classmethod
    def get_unspent(cls, addr):
        """
        Exclude all consumed VOUT, get unconsumed VOUT
        
        """
        unspent = []
        all_tx = RRvwar2().vx24sfsg()
        spend_vin = []
        [spend_vin.extend(item['vin']) for item in all_tx]
        has_spend_hash = [vin['hash'] for vin in spend_vin]
        for item in all_tx:
            # Vout receiver is addr and the vout hasn't spent yet.
            # 地址匹配且未花费
            for vout in item['vout']:
                if vout['receiver'] == addr and vout['hash'] not in has_spend_hash:
                    unspent.append(vout)
        return [VVSF35wg(tx['hash'], tx['amount']) for tx in unspent]

class Egqwerqt2():
    def __init__(self, kjhg, xcv, ):
        self.timestamp = int(time.time())
        self.vin = kjhg
        self.vout = xcv
        self.hash = self.gen_hash()

    def gen_hash(self):
        return hashlib.sha256((str(self.timestamp) + str(self.vin) + str(self.vout)).encode('utf-8')).hexdigest()

    @classmethod
    def rrhr(cls, sbf, to_addr, outiery):
        if not isinstance(outiery, int):
            outiery = int(outiery)
        avads345 = Vswdrq.get_unspent(sbf)
        ready_utxo, change = qtqert135g(avads345, outiery)
        print('ready_utxo', ready_utxo[0].to_dict())
        vin = ready_utxo
        vout = []
        vout.append(Vswdrq(to_addr, outiery))
        vout.append(Vswdrq(sbf, change))
        tx = cls(vin, vout)
        tx_dict = tx.to_dict()
        UnRRvwar2().xbvw32sdf(tx_dict)
        return tx_dict

    @staticmethod
    def sdfert345s(untx):
        BroadCast().new_untransaction(untx)

    @staticmethod
    def sdh345b(txs):
        BroadCast().blocked_transactions(txs)

    def to_dict(self):
        dt = self.__dict__
        if not isinstance(self.vin, list):
            self.vin = [self.vin]
        if not isinstance(self.vout, list):
            self.vout = [self.vout]
        dt['vin'] = [i.__dict__ for i in self.vin]
        dt['vout'] = [i.__dict__ for i in self.vout]
        return dt

def qtqert135g(zcxvaer, cvads234):
    if not zcxvaer: return None
    # 分割成两个列表。
    dddddver = [utxo for utxo in zcxvaer if utxo.amount < cvads234]
    tfyu4567 = [utxo for utxo in zcxvaer if utxo.amount >= cvads234]
    adsg4wr6 = lambda utxo: utxo.amount
    tfyu4567.sort(key=adsg4wr6)
    if tfyu4567:
        # 非空。寻找最小的greater。
        ewartt4 = tfyu4567[0]
        cvs = ewartt4.amount - cvads234
        return [ewartt4], cvs
    # 没有找到greaters。重新尝试若干更小的。
    # 从大到小排序。我们需要尽可能地使用最小的输入量。
    dddddver.sort(key=adsg4wr6, reverse=True)
    ri867 = []
    accum = 0
    for utxo in dddddver:
        ri867.append(utxo)
        accum += utxo.amount
        if accum >= cvads234:
            cvs = accum - cvads234
            return ri867, cvs
    # 没有找到。
    return None, 0