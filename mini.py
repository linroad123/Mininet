from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink

net = Mininet(host=CPULimitedHost,link=TCLink)

# Creating nodes in the network
c0 = net.addController()
h0 = net.addHost('h0')
s0 = net.addSwitch('s0')
h1 = net.addHost('h1',cpu=0.5)
h2 = net.addHost('h2',cpu=0.5)

# Creating links between nodes in network
net.addLink(s0,h0,bw=10,delay='5ms',max_queue_size=1000,loss=10,use_htb=True)
net.addLink(h1,s0)
net.addLink(h2,s0)

# Configuration of IP address in interfaces
h0.setIP('192.168.1.1',24)
h1.setIP('192.168.1.2',24)
net.start()
net.pingAll()
net.stop()