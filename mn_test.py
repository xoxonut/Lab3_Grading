from mininet.net import Mininet
from itertools import permutations
def arpingall(net:Mininet):
    for src, dst in permutations(net.hosts,2):
        src.cmdPrint('arping -c1', dst.IP())
                
tests = {'arpingall':arpingall}