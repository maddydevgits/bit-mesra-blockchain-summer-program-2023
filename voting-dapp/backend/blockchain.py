from web3 import Web3,HTTPProvider
import json

artifact='../build/contracts/voting.json'
artifact1='../build/contracts/register.json'

def connect_with_blockchain(wallet):
    server='http://127.0.0.1:7545'

    web3=Web3(HTTPProvider(server))
    web3.eth.defaultAccount=wallet

    with open(artifact) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
        contract_address=contract_json['networks']['5777']['address']
    
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )

    return (contract,web3)

def connect_with_blockchain_register(wallet):
    server='http://127.0.0.1:7545'

    web3=Web3(HTTPProvider(server))
    web3.eth.defaultAccount=wallet

    with open(artifact1) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
        contract_address=contract_json['networks']['5777']['address']
    
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )

    return (contract,web3)