# coding:utf-8
from xmlrpc.server import SimpleXMLRPCServer  
from xmlrpc.client import ServerProxy
from node import sdbawehy234, nh56
from database import VDRFwrv234, UnRRvwar2, RRvwar2
from lib.common import cprint
server = None

PORT = 8301

class Rvsdfs():

    def __init__(self, vvs35sf23):
        self.server = vvs35sf23

    def iytwer(self):
        return True
    
    def kger(self):
        bcdb = VDRFwrv234()
        return bcdb.vx24sfsg()

    def nwet35(self, block):
        cprint('RPC', block)
        VDRFwrv234().xbvw32sdf(block)
        UnRRvwar2().clear()
        cprint('INFO',"Receive new block.")
        return True

    def vsdr23t6sf(self):
        sdfa23 = RRvwar2()
        return sdfa23.vx24sfsg()

    def sfdkru(self, untx):
        cprint(__name__,untx)
        UnRRvwar2().xbvw32sdf(untx)
        cprint('INFO',"Receive new unchecked transaction.")
        return True

    def cxb2345(self, txs):
        RRvwar2().asf51414df(txs)
        cprint('INFO',"Receive new blocked transactions.")
        return True

    def add_node(self, address):
        nh56(address)
        return True

class R3fsh():

    ALLOW_METHOD = ['get_transactions', 'get_blockchain', 'new_block', 'new_untransaction', 'blocked_transactions', 'ping', 'add_node']

    def __init__(self, node):
        self.node = node
        self.client = ServerProxy(node)
    
    def __getattr__(self, name):
        def noname(*args, **kw):
            if name in self.ALLOW_METHOD:
                return getattr(self.client, name)(*args, **kw)
        return noname

class BroadCast():

    def __getattr__(self, name):
        def noname(*args, **kw):
            cs = get_clients()
            rs = []
            for c in cs:
                try:
                    rs.append(getattr(c,name)(*args, **kw))
                except ConnectionRefusedError:
                    cprint('WARN', 'Contact with node %s failed when calling method %s , please check the node.' % (c.node,name))
                else:
                    cprint('INFO', 'Contact with node %s successful calling method %s .' % (c.node,name))
            return rs
        return noname

def start_server(ip, port=8301):
    server = SimpleXMLRPCServer((ip, port))
    rpc = Rvsdfs(server)
    server.register_instance(rpc)
    server.serve_forever()

def get_clients():
    clients = []
    nodes = sdbawehy234()

    for node in nodes:
        clients.append(R3fsh(node))
    return clients