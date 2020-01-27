#!/usr/bin/env python3
"""
@summary: send tranactions with jmeter 

@version: v52 (22/January/2019)
@since:   17/April/2018
@author:  https://github.com/drandreaskrueger
@see:     https://github.com/drandreaskrueger/chainhammer for updates
"""

# extend sys.path for imports:
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

################
## Dependencies:

# standard library:
import sys, time, random, json
from threading import Thread
from queue import Queue
from pprint import pprint
from subprocess import Popen, DEVNULL

# pypi:
import requests # pip3 install requests
import web3
from web3 import Web3, HTTPProvider # pip3 install web3
from web3.utils.encoding import pad_hex

#chain: hammer
from hammer.config import RPCaddress,FILE_LAST_EXPERIMENT, EMPTY_BLOCKS_AT_END
from hammer.clienttools import web3connection, unlockAccount

#  Harcoding success , num of transactions while debugging
# def store_experiment_data(success=True, num_txs=5000, 
#                           block_from, block_to, 
#                           empty_blocks=10,
#                           filename=FILE_LAST_EXPERIMENT):

w3, chainInfos = web3connection(RPCaddress=RPCaddress, account=None)

block_from = w3.eth.blockNumber

def send_jmeter():
    # block_from = w3.eth.blockNumber
    # p = Popen(["./jmeter.sh"], stdout=DEVNULL)
    Account = w3.eth.accounts[0]
    p = Popen(["./jmeter.sh", "RPCaddress","Account"])
    p.wait()
    block_to = w3.eth.blockNumber

    print ("Jmeter is done")
    filename=FILE_LAST_EXPERIMENT
    data = {"send" : {
                "block_first" : block_from,
                "block_last": block_to,
                "empty_blocks": 10, 
                "num_txs" : 5000,
                "sample_txs_successful": True
                },
            "node" : {
                "rpc_address": RPCaddress,
                "web3.version.node": w3.version.node,
                "name" : NODENAME,
                "type" : NODETYPE,
                "version" : NODEVERSION, 
                "consensus" : CONSENSUS, 
                "network_id" : NETWORKID, 
                "chain_name" : CHAINNAME, 
                "chain_id" : CHAINID
                }
            }
            
    with open(filename, "w") as f:
        json.dump(data, f)
    print(block_from, block_to)



if __name__ == '__main__':
    global w3, NODENAME, NODETYPE, NODEVERSION, CONSENSUS, NETWORKID, CHAINNAME, CHAINID
    w3, chainInfos = web3connection(RPCaddress=RPCaddress, account=None)
    NODENAME, NODETYPE, NODEVERSION, CONSENSUS, NETWORKID, CHAINNAME, CHAINID = chainInfos
    send_jmeter()






