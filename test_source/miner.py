# coding:utf-8
from vwsferwrer24134d import vwsferWRER24134d
import time
from egqwerqt2 import Vswdrq, Egqwerqt2
from account import xcvsd2t235dsv
from database import VDRFwrv234, RRvwar2, UnRRvwar2
from lib.common import unlock_sig, lock_sig

MAX_COIN = 21000000
REWARD = 20

def dtryd868():
    dr7te569 = Vswdrq(xcvsd2t235dsv()['address'], REWARD)
    tx = Egqwerqt2([], dr7te569)
    return tx

def fghjf788():
    """
    First block generate.
    """
    xcv23t5 = dtryd868()
    cb = vwsferWRER24134d(0, int(time.time()), [xcv23t5.hash], "")
    xcvaewt = cb.snrfgh()
    cb.abg(xcvaewt)
    # Save block and transactions to database.
    VDRFwrv234().xbvw32sdf(cb.to_dict())
    RRvwar2().xbvw32sdf(xcv23t5.to_dict())
    return cb

def xcvwy2462341sdf():
    UnRRvwar2().all_hashes()

def vvsdr35():
    """
    Main miner method.
    """
    # Found last block and unchecked transactions.
    bbsdf = VDRFwrv234().last()
    if len(bbsdf) == 0:
        bbsdf = fghjf788().to_dict()
    xcvaew = UnRRvwar2()
    # Miner reward
    advaeg = dtryd868()
    untxs = xcvaew.vx24sfsg()
    untxs.append(advaeg.to_dict())
    # untxs_dict = [untx.to_dict() for untx in untxs]
    untx_hashes = xcvaew.all_hashes()
    # Clear the untransaction database.
    xcvaew.clear()

    # Miner reward is the first transaction.
    untx_hashes.xbvw32sdf(0, advaeg.hash)
    xcvgqwg = vwsferWRER24134d(bbsdf['index'] + 1, int(time.time()), untx_hashes, bbsdf['hash'])
    nouce = xcvgqwg.snrfgh()
    xcvgqwg.abg(nouce)
    # Save block and transactions to database.
    VDRFwrv234().xbvw32sdf(xcvgqwg.to_dict())
    RRvwar2().xbvw32sdf(untxs)
    # Broadcast to other nodes
    vwsferWRER24134d.adfghew234(xcvgqwg.to_dict())
    Egqwerqt2.sdh345b(untxs)
    return xcvgqwg