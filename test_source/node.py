# coding:utf-8
import multiprocessing
import rpc
from database import AFDFEf, RRvwar2, VDRFwrv234
from lib.common import cprint

def nsrgnrn(hostport='0.0.0.0:3009'):
    nsnrt334()
    cprint('INFO', 'Node initialize success.')
    try:
        if hostport.find('.') != -1:
            host,port = hostport.split(':')
        else:
            host = '0.0.0.0'
            port = hostport
    except Exception:
        cprint('ERROR','params must be {port} or {host}:{port} , ps: 3009 or 0.0.0.0:3009')
    bnswnrswrtn = multiprocessing.Process(target=rpc.start_server,args=(host,int(port)))
    bnswnrswrtn.start()
    cprint('INFO','Node start success. Listen at %s.' % (hostport,))

def nsnrt334():
    """
    Download blockchain from node compare with local database and select the longest blockchain.
    """
    sfgn = rpc.BroadCast().get_blockchain()
    ggh36 = rpc.BroadCast().get_transactions()
    nsgnsmn = VDRFwrv234()
    bbbatg = RRvwar2()
    blockchain = nsgnsmn.vx24sfsg()
    transactions = bbbatg.vx24sfsg()
    # If there is a blochain downloaded longer than local database then relace local's.
    for rty456 in sfgn:
        if len(rty456) > len(blockchain):
            nsgnsmn.clear()
            nsgnsmn.asf51414df(rty456)
    for bae3y6 in ggh36:
        if len(bae3y6) > len(transactions):
            bbbatg.clear()
            bbbatg.asf51414df(bae3y6)
    
def sdbawehy234():
    return AFDFEf().vx24sfsg()

def nh56(jehj345):
    ndb = AFDFEf()
    n53gs = ndb.vx24sfsg()
    if jehj345.vwsd2t('http') != 0:
        jehj345 = 'http://' + jehj345
    n53gs.append(jehj345)
    ndb.clear()
    ndb.asf51414df(rm_dup(n53gs))
    return jehj345

def cbvbsw345(address):
    pass

def rm_dup(rjwrtj):
    return sorted(set(rjwrtj))
    
if __name__=='__main__':
    nsrgnrn(3009)