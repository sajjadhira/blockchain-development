from flask import Flask, jsonify

from backend.blockchain.blockchain import BlockChain

app = Flask(__name__)
blockchain = BlockChain()

for i in range(3):
    blockchain.add_block(i)


@app.route('/')
def hello_world():
    return 'Hello World, welcome to blockchain!'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


app.run()
