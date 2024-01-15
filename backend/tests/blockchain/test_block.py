from backend.blockchain.block import Block, GENESIS_DATA


def test_mine_block():
    """
    mine_block: Create a block and add it to the blockchain.
    """
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash


def test_genesis():
    """
    genesis: Generate the genesis block.
    """
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        assert getattr(Block.genesis(), key) == value
