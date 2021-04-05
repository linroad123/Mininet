from pyretic.lib.corelib import *
from pyretic.lib.std import *

# insert the name of the module and policy you want to import
import os
from pox.lib.addresses import IPAddr, EthAddr
from pyretic.modules.mac_learner import mac_learner

policy_file = "blocked_macs.csv" 

def main():
    # start with a policy that doesn't match any packets
    not_allowed = none
    # and add traffic that isn't allowed
    # for <each pair of MAC address in firewall-policies.csv>:
    #     not_allowed = not_allowed + ( <traffic going in one direction> ) + ( <traffic going in the other direction> )
    with open(policy_file) as f:
        #line = f.readline()
        #print line
        line = f.readline().strip()
        while line:
            print("policy: {}".format(line))
            smac, dmac = line.split(',')
            rule1 = match(srcmac=MAC(smac)) & match(dstmac=MAC(dmac))
            rule2 = match(dstmac=MAC(smac)) & match(srcmac=MAC(dmac))
            not_allowed = not_allowed + rule1 + rule2
            line = f.readline().strip()

    # express allowed traffic in terms of not_allowed - hint use '~'
    
    allowed = ~ not_allowed

    # and only send allowed traffic to the mac learning (act_like_switch) logic
    return allowed >> flood()