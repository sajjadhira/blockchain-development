from backend.blockchain.block import Block, GENESIS_DATA
from backend.blockchain.blockchain import BlockChain


def tets_blockchain_instance():
    blockchain = BlockChain()

    assert blockchain.chain[0].hash == GENESIS_DATA['hash']


def test_add_block():
    blockchain = BlockChain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data
