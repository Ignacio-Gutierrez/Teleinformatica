#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='192.168.100.0/26')

    info( '*** Adding controller\n' )
    info( '*** Add routers\n')
    r0 = net.addHost('r0', ip='192.168.100.6/29')

    r1 = net.addHost('r1', ip='192.168.100.1/29')
    r2 = net.addHost('r2', ip='192.168.100.9/29')
    r3 = net.addHost('r3', ip='192.168.100.17/29')
    r4 = net.addHost('r4', ip='192.168.100.25/29')
    r5 = net.addHost('r5', ip='192.168.100.33/29')
    r6 = net.addHost('r6', ip='192.168.100.41/29')
    
    info( '*** Add switches\n')
    s1_a = net.addSwitch('s1_a', cls=OVSKernelSwitch, failMode='standalone')
    s1_b = net.addSwitch('s1_b', cls=OVSKernelSwitch, failMode='standalone')

    s2_a = net.addSwitch('s2_a', cls=OVSKernelSwitch, failMode='standalone')
    s2_b = net.addSwitch('s2_b', cls=OVSKernelSwitch, failMode='standalone')

    s3_a = net.addSwitch('s3_a', cls=OVSKernelSwitch, failMode='standalone')
    s3_b = net.addSwitch('s3_b', cls=OVSKernelSwitch, failMode='standalone')

    s4_a = net.addSwitch('s4_a', cls=OVSKernelSwitch, failMode='standalone')
    s4_b = net.addSwitch('s4_b', cls=OVSKernelSwitch, failMode='standalone')

    s5_a = net.addSwitch('s5_a', cls=OVSKernelSwitch, failMode='standalone')
    s5_b = net.addSwitch('s5_b', cls=OVSKernelSwitch, failMode='standalone')

    s6_a = net.addSwitch('s6_a', cls=OVSKernelSwitch, failMode='standalone')
    s6_b = net.addSwitch('s6_b', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.254/24', defaultRoute='via 10.0.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.254/24', defaultRoute='via 10.0.2.1')
    h3 = net.addHost('h3', cls=Host, ip='10.0.3.254/24', defaultRoute='via 10.0.3.1')
    h4 = net.addHost('h4', cls=Host, ip='10.0.4.254/24', defaultRoute='via 10.0.4.1')
    h5 = net.addHost('h5', cls=Host, ip='10.0.5.254/24', defaultRoute='via 10.0.5.1')
    h6 = net.addHost('h6', cls=Host, ip='10.0.6.254/24', defaultRoute='via 10.0.6.1')
    
    info( '*** Add links\n')
    net.addLink(s1_a, r0, intfName1='s1_a-eth1', intfName2='r0-eth1', params2={'ip':'192.168.100.6/29'})
    net.addLink(s1_a, r1, intfName1='s1_a-eth2', intfName2='r1-eth1', params2={'ip':'192.168.100.1/29'})
    net.addLink(s1_b, r1, intfName1='s1_b-eth1', intfName2='r1-eth2', params2={'ip':'10.0.1.1/24'})
    net.addLink(s1_b, h1, intfName1='s1_b-eth2', intfName2='h1-eth1', params2={'ip':'10.0.1.254/24'})

    net.addLink(s2_a, r0, intfName1='s2_a-eth1', intfName2='r0-eth2', params2={'ip':'192.168.100.14/29'})
    net.addLink(s2_a, r2, intfName1='s2_a-eth2', intfName2='r2-eth1', params2={'ip':'192.168.100.9/29'})
    net.addLink(s2_b, r2, intfName1='s2_b-eth1', intfName2='r2-eth2', params2={'ip':'10.0.2.1/24'})
    net.addLink(s2_b, h2, intfName1='s2_b-eth2', intfName2='h2-eth1', params2={'ip':'10.0.2.254/24'})

    net.addLink(s3_a, r0, intfName1='s3_a-eth1', intfName2='r0-eth3', params2={'ip':'192.168.100.22/29'})
    net.addLink(s3_a, r3, intfName1='s3_a-eth2', intfName2='r3-eth1', params2={'ip':'192.168.100.17/29'})
    net.addLink(s3_b, r3, intfName1='s3_b-eth1', intfName2='r3-eth2', params2={'ip':'10.0.3.1/24'})
    net.addLink(s3_b, h3, intfName1='s3_b-eth2', intfName2='h3-eth1', params2={'ip':'10.0.3.254/24'})

    net.addLink(s4_a, r0, intfName1='s4_a-eth1', intfName2='r0-eth4', params2={'ip':'192.168.100.30/29'})
    net.addLink(s4_a, r4, intfName1='s4_a-eth2', intfName2='r4-eth1', params2={'ip':'192.168.100.25/29'})
    net.addLink(s4_b, r4, intfName1='s4_b-eth1', intfName2='r4-eth2', params2={'ip':'10.0.4.1/24'})
    net.addLink(s4_b, h4, intfName1='s4_b-eth2', intfName2='h4-eth1', params2={'ip':'10.0.4.254/24'})
    
    net.addLink(s5_a, r0, intfName1='s5_a-eth1', intfName2='r0-eth5', params2={'ip':'192.168.100.38/29'})
    net.addLink(s5_a, r5, intfName1='s5_a-eth2', intfName2='r5-eth1', params2={'ip':'192.168.100.33/29'})
    net.addLink(s5_b, r5, intfName1='s5_b-eth1', intfName2='r5-eth2', params2={'ip':'10.0.5.1/24'})
    net.addLink(s5_b, h5, intfName1='s5_b-eth2', intfName2='h5-eth1', params2={'ip':'10.0.5.254/24'})

    net.addLink(s6_a, r0, intfName1='s6_a-eth1', intfName2='r0-eth6', params2={'ip':'192.168.100.46/29'})
    net.addLink(s6_a, r6, intfName1='s6_a-eth2', intfName2='r6-eth1', params2={'ip':'192.168.100.41/29'})
    net.addLink(s6_b, r6, intfName1='s6_b-eth1', intfName2='r6-eth2', params2={'ip':'10.0.6.1/24'})
    net.addLink(s6_b, h6, intfName1='s6_b-eth2', intfName2='h6-eth1', params2={'ip':'10.0.6.254/24'})

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1_a').start([])
    net.get('s1_b').start([])

    net.get('s2_a').start([])
    net.get('s2_b').start([])

    net.get('s3_a').start([])
    net.get('s3_b').start([])

    net.get('s4_a').start([])
    net.get('s4_b').start([])

    net.get('s5_a').start([])
    net.get('s5_b').start([])

    net.get('s6_a').start([])
    net.get('s6_b').start([])

    info( '*** Post configure switches and hosts\n')

    r0.cmd('sysctl net.ipv4.ip_forward=1')
    r0.cmd('ip route add 10.0.1.0/24 via 192.168.100.1\
         && ip route add 10.0.2.0/24 via 192.168.100.9 \
         && ip route add 10.0.3.0/24 via 192.168.100.17 \
         && ip route add 10.0.4.0/24 via 192.168.100.25 \
         && ip route add 10.0.5.0/24 via 192.168.100.33 \
         && ip route add 10.0.6.0/24 via 192.168.100.41')


    r1.cmd('sysctl net.ipv4.ip_forward=1')
    r1.cmd('ip route add 10.0.0.0/21 via 192.168.100.6 && \
            ip route add 192.168.100.0/26 via 192.168.100.6')

    r2.cmd('sysctl net.ipv4.ip_forward=1')
    r2.cmd('ip route add 10.0.0.0/21 via 192.168.100.14 && \
            ip route add 192.168.100.0/26 via 192.168.100.14')
    
    r3.cmd('sysctl net.ipv4.ip_forward=1')
    r3.cmd('ip route add 10.0.0.0/21 via 192.168.100.22 && \
            ip route add 192.168.100.0/26 via 192.168.100.22')

    r4.cmd('sysctl net.ipv4.ip_forward=1')
    r4.cmd('ip route add 10.0.0.0/21 via 192.168.100.30 && \
            ip route add 192.168.100.0/26 via 192.168.100.30')

    r5.cmd('sysctl net.ipv4.ip_forward=1')
    r5.cmd('ip route add 10.0.0.0/21 via 192.168.100.38 && \
            ip route add 192.168.100.0/26 via 192.168.100.38')

    r6.cmd('sysctl net.ipv4.ip_forward=1')
    r6.cmd('ip route add 10.0.0.0/21 via 192.168.100.46 && \
            ip route add 192.168.100.0/26 via 192.168.100.46')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

