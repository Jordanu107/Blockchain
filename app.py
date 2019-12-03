from uuid import uuid4
from blockchain import Blockchain
from requests import request

import flask

# Instantiate node
app = flask.Flask(__name__)

# Generate a globally unique address for this node
node_id = str(uuid4()).replace('-','')

# Instantiate blockchain
new_blockchain = Blockchain()


@app.route('/', methods=['GET'])
def homepage():
    return "Welcome to my blockchain page!"


@app.route('/mine', methods=['GET'])
def mine():
    last_block = new_blockchain.last_block
    last_proof = last_block.proof
    proof = new_blockchain.proof_of_work(last_proof)

    # Reward the miner by adding a transaction to give miner coins
    new_blockchain.new_transaction("0", node_id, 1)

    # Forge new block by adding to chain
    previous_hash = new_blockchain.hash_block(last_block)
    block = new_blockchain.new_block(previous_hash, proof)

    response = {
        'message': "New Block Forged",
        "index": block.index,
        "transactions": block.transactions,
        "proof": block.proof,
        "previous_hash": block.previous_hash
    }

    return flask.jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    values = request.get_json()
    required_values = ['sender', 'receiver', 'amount']

    # Missing information for a transaction
    if not [value for value in values] == required_values:
        return 'Missing values', 400

    # Create new transaction and send a success response to the user
    index = new_blockchain.new_transaction(values['sender'], values['receiver'], values['amount'])
    response = {'message': 'Transaction will be added to Block %d' % index}
    return flask.jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': new_blockchain.stringify_chain(),
        'length': len(new_blockchain.chain)
    }
    return flask.jsonify(response), 200


if __name__ == "__main__":
    app.run(port=5000)