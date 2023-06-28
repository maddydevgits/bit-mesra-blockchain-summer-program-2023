from flask import Flask,request
from blockchain import *

# create an object
api=Flask(__name__)

@api.route('/')
def home():
    return('API Server is Online')

# create api for casting vote
@api.route('/castvote',methods=['get','post'])
def castvote():
    id=request.args.get('id')
    wallet=request.args.get('wallet')
    print(id)
    try:
        contract,web3=connect_with_blockchain(wallet)
        tx_hash=contract.functions.castVote(int(id)).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return ('You have voted for {0}, the txhash is {1}'.format(id,tx_hash))
    except:
        return('You have already voted')


if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )
