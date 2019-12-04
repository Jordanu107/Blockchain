from transaction import Transaction
from block import Block
from time import time
import json
import hashlib


# Blueprint of a blockchain
class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(0, 100)  # Create the genesis block

    def new_block(self, previous_hash, proof):
        """
        Creates a new block and adds it to the existing chain
        :param previous_hash: <str>
        :param proof: <int>
        :return: <block>
        """
        current_block = Block(len(self.chain) + 1, time(),
                              self.current_transactions, previous_hash, proof)

        # Delete all the transactions added to the new block
        self.current_transactions = []

        self.chain.append(current_block)
        return current_block

    def new_transaction(self, sender, receiver, amount):
        """
        Adds a transaction to a list of current transactions
        :param sender: <user>
        :param receiver: <user>
        :param amount: <int>
        :return: <int> Index of the next block, the one that has yet to be mined
        """
        current_transaction = Transaction(sender, receiver, amount)
        self.current_transactions.append(vars(current_transaction))
        return self.last_block.index + 1

    # Returns the most recent block added to the chain
    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash_block(block):
        """
        Hashes a block with SHA256 hash algorithm
        :param block: <block>
        :return: <str>
        """

        encoded_block = json.dumps(vars(block), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm - Find a number p', such that hash(pp')
        contains 3 trailing zeros, where p is the previous proof and p' is
        the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0

        while not self.valid_proof(last_proof, proof):
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof, proof) have 3 trailing zeroes
        :param last_proof: <int> Previous proof
        :param proof: <int> Current proof
        :return: <bool> True if correct, otherwise false

        NOTE: for more info, see: https://en.wikipedia.org/wiki/Hashcash
        """

        guess = ("%s%s" % (last_proof, proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[-3:] == "000"

    def stringify_chain(self):
        new_chain = []
        for block in self.chain:
            new_chain.append({
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "proof": block.proof,
                "previous_hash": block.previous_hash
            })
        return new_chain