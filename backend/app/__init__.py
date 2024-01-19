import os
import requests
import random

from flask import Flask, jsonify

from backend.blockchain.blockchain import BlockChain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = BlockChain()
pubsub = PubSub(blockchain)


@app.route('/')
def hello_world():
    return 'Hello World, welcome to blockchain!'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = f'BTC SENT TO SAJJAD: {random.randint(100, 1000)}'

    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())


ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)
    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    print(result.json())
    result_blockchain = BlockChain.from_json(result.json())
    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully synchronized the local chain')
    except Exception as e:
        print(f'\n -- Error synchronizing: {e}')

app.run(port=PORT)
