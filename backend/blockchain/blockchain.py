
from backend.blockchain.block import Block, GENESIS_DATA


class BlockChain:
    """
    BlockChain: A public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'BlockChain: {self.chain}'


def main():

    blockchain = BlockChain()
    blockchain.add_block('one')
    print(blockchain.chain[0].hash == GENESIS_DATA['hash'])
    # blockchain.add_block('two')
    # blockchain.add_block('three')
    # print(blockchain)
    # print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()
