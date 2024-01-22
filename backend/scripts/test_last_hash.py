import requests

from backend.blockchain.block import Block


chain = requests.get('http://localhost:5000/blockchain').json()
for i in range(1, len(chain)):
    block = chain[i]
    last_block = chain[i-1]
    print("\n\n-----------------------\n\n")
    print(f'{last_block["hash"]}')
    print(f'{block["last_hash"]}')
    print("\n\n-----------------------\n\n")
