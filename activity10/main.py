# Web3

from web3 import Web3,HTTPProvider
import json

artifact="../build/contracts/voting.json"

def connect_with_blockchain(wallet):
    # Blockchain Server
    blockchainServer='http://127.0.0.1:7545'
    # web3 object connects with server
    web3=Web3(HTTPProvider(blockchainServer))
    
    # accessing abi, address
    with open(artifact) as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    
    # from which wallet
    web3.eth.defaultAccount=wallet

    # contract instance to which wallet has to connect
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )
    return(contract,web3)

contract,web3=connect_with_blockchain('0xEf738aB46F9eA6f5649EeDc26867f0Eb611976A3')

# tx_hash=contract.functions.castVote(1).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
# print('Vote Casted')

_votes=contract.functions.displayVotes().call()
print(_votes)

