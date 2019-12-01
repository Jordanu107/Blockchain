import transaction
import block

# Blueprint of a blockchain
class Blackchain(object):

    # New blockchain will be initially empty
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # Creates a new block and adds it to the chain
    def new_block(self):
        pass

    def new_transaction(self, sender, receiver, amount):
        """
        Adds a transaction to a list of current transactions
        :param sender:
        :param receiver:
        :param amount:
        :return: Index of the next block, the one that has yet to be mined
        """
        current_transaction = transaction.Transaction(sender, receiver, amount)
        self.current_transactions.append(current_transaction)
        return self.last_block['index'] + 1

    # Hashes a block
    @staticmethod
    def hash_block(block):
        pass

    # Returns the most recent block added to the chain
    @property
    def last_block(block):
        pass