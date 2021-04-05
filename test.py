from mininet.net import Mininet
from mininet.topolib import TreeTopo
from mininet.log import setLogLevel, info, error
from mininet.util import dumpNodeConnections

Tree222 = TreeTopo(depth=3,fanout=2)
net = Mininet(topo=Tree222)
info( '*** Starting network\n')
net.start()
dumpNodeConnections(net.hosts)
dumpNodeConnections(net.switches)
net.pingAll()
info( '*** Stopping network' )
net.stop()