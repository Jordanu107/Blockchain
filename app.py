from uuid import uuid4
from blockchain import Blockchain

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
    return "We'll mine a new Block!"


@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': new_blockchain.stringify_chain(),
        'length': len(new_blockchain.chain)
    }
    return flask.jsonify(response), 200


if __name__ == "__main__":
    app.run(port=5000)