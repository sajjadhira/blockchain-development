import time
from backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'dificulty': 3,
    'nonce': 'genesis_nonce'
}


class Block:
    """
    Block: A unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data, dificulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.dificulty = dificulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'data: {self.dificulty}, '
            f'data: {self.nonce})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        mine_block: Create a block and add it to the blockchain.
        Mine a block based on the given last_block and data, until a block hash
        is found that meets the leading 0's proof of work requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        dificulty = last_block.dificulty
        nonce = 0
        # hash = f'{timestamp}-{last_hash}'
        hash = crypto_hash(timestamp, last_hash, data, dificulty, nonce)

        while hash[0:dificulty] != '0' * dificulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, dificulty, nonce)

        return Block(timestamp, last_hash, hash, data, dificulty, nonce)

    @staticmethod
    def genesis():
        """
        genesis: Generate the genesis block.
        """
        return Block(**GENESIS_DATA)


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == '__main__':
    main()
