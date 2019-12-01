from transaction import Transaction
from block import Block
import time

# Blueprint of a blockchain
class Blackchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block = Block(1, 100) # Create the genesis block

    def new_block(self, previous_hash, proof):
        """
        Creates a new block and adds it to the existing chain
        :param previous_hash:
        :param proof:
        :return: the added block
        """
        current_block = Block(len(self.chain) + 1, time.time(),
                              self.current_transactions, previous_hash, proof)

        # Delete all the transactions added to the new block
        self.current_transactions = []

        self.chain.append(current_block)
        return current_block

    def new_transaction(self, sender, receiver, amount):
        """
        Adds a transaction to a list of current transactions
        :param sender:
        :param receiver:
        :param amount:
        :return: Index of the next block, the one that has yet to be mined
        """
        current_transaction = Transaction(sender, receiver, amount)
        self.current_transactions.append(current_transaction)
        return self.last_block['index'] + 1

    # Returns the most recent block added to the chain
    @property
    def last_block(self):
        return self.chain[-1]

    # Hashes a block
    @staticmethod
    def hash_block(block):
        pass