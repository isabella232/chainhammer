#!/usr/bin/env python3


# extend path for imports:
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# standard library:
import sys, time, random, json, os , re, subprocess
from threading import Thread
from queue import Queue
from pprint import pprint

import subprocess
from urllib.parse import urlparse

# pypi:
import requests # pip3 install requests
import web3
from web3 import Web3, HTTPProvider # pip3 install web3
from web3.utils.abi import filter_by_name, abi_to_signature
from web3.utils.encoding import pad_hex

# chainhammer:
from hammer.config import RPCaddress, ROUTE, PRIVATE_FOR, EXAMPLE_ABI
from hammer.config import PARITY_UNLOCK_EACH_TRANSACTION
from hammer.config import GAS_FOR_SET_CALL
from hammer.config import FILE_LAST_EXPERIMENT, EMPTY_BLOCKS_AT_END
from hammer.clienttools import web3connection, unlockAccount


def send_transactions(rpc , account):
    with open(os.devnull, 'w') as fp:
        cmd = subprocess.Popen(["./jmeter.sh", rpc, account], stdout=fp)
        cmd.wait()
        block_to = w3.eth.blockNumber

    empty_blocks = EMPTY_BLOCKS_AT_END
    success = True
    filename=FILE_LAST_EXPERIMENT
    
    data = {"send" : {
                "block_first" : block_from,
                "block_last": block_to,
                "empty_blocks": empty_blocks, 
                "num_txs" : 10000,
                "sample_txs_successful": success
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

if __name__ == '__main__':
    
    # check_CLI_or_syntax_info_and_exit()

    global w3, NODENAME, NODETYPE, NODEVERSION, CONSENSUS, NETWORKID, CHAINNAME, CHAINID
    w3, chainInfos = web3connection(RPCaddress=RPCaddress, account=None)
    NODENAME, NODETYPE, NODEVERSION, CONSENSUS, NETWORKID, CHAINNAME, CHAINID = chainInfos


    block_from = w3.eth.blockNumber
    print(block_from)
    # rpc =  RPCaddress[7:]
    rpc = urlparse(RPCaddress)
    account = w3.eth.accounts[0]    
    send_transactions(str(rpc.hostname) , account)
    # print(block_from, block_to)

    # store_experiment_data
