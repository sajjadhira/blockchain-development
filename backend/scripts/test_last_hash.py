import requests
from backend.blockchain.block import Block

from backend.blockchain.blockchain import BlockChain
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary


blockchain = requests.get('http://localhost:5000/blockchain')
result_blockchain = BlockChain.from_json(blockchain.json())

chain = result_blockchain.chain

block = chain[-1]

block_hash = block.hash
reconstructed_hash = crypto_hash(
    block.timestamp,
    block.last_hash,
    block.data,
    block.difficulty,
    block.nonce
)

print(f'block_hash: {block_hash}')
print(f'reconstructed_hash: {reconstructed_hash}')

# df = hex_to_binary(block.hash)[0:block.difficulty]
# df2 = '0' * block.difficulty

# dfdf = df == df2
# computing = Block.computing(block.hash, block.difficulty)
# print(f'last_block: {dfdf}')
# print(f'last_block: {df2}')


# for i in range(1, len(chain)):
#     block = chain[i]
#     last_block = chain[i-1]

#     block_hash = block.hash
#     reconstructed_hash = crypto_hash(
#         block.timestamp,
#         block.last_hash,
#         block.data,
#         block.difficulty,
#         block.nonce
#     )
#     print(f'block_ hash: {block_hash}')
#     print(f'reconstructed_hash: {reconstructed_hash}')

#     # Block.is_valid_block(last_block, block)

#     print("\n\n--------------------\n\n")
