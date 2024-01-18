import pytest

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


@pytest.fixture
def blockchain_three_blocks():
    blockchain = BlockChain()

    for i in range(3):
        blockchain.add_block(i)

    return blockchain


def test_is_valid_chain(blockchain_three_blocks):

    BlockChain.is_valid_chain(blockchain_three_blocks.chain)


def test_is_valid_chain_bad_genesis(blockchain_three_blocks):
    blockchain_three_blocks.chain[0].hash = 'evil_hash'

    with pytest.raises(Exception, match='genesis block must be valid'):
        BlockChain.is_valid_chain(blockchain_three_blocks.chain)
