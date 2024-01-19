
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

    def replace_chain(self, chain):
        """
        replace_chain: Replace the local chain with the incoming one if the following applies:
            - The incoming chain is longer than the local one.
            - The incoming chain is formatted properly.
        """
        if (len(chain) <= len(self.chain)):
            raise Exception(
                'Cannto replace. The incoming chain must be longer.')

        try:
            BlockChain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(
                f'Cannot replace. The incoming chain is invalid: {e}')

        self.chain = chain

    def to_json(self):
        """
        Serialize the blockchain into a list of blocks.
        """
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def is_valid_chain(chain):
        """
        is_valid_chain: Validate the incoming chain.
        Enforce the following rules of the blockchain:
            - the chain must start with the genesis block
            - blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


def main():

    blockchain = BlockChain()
    # blockchain.add_block('one')
    # print(blockchain.chain[0].hash == GENESIS_DATA['hash'])
    # blockchain.add_block('two')
    # blockchain.add_block('three')
    # print(blockchain)
    # print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()
