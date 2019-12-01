class Block(object):

    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def __str__(self):
        return str(self.index) + str(self.timestamp) + self.transactions + \
               self.proof + self.previous_hash