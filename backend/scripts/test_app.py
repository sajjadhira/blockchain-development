import random
import requests
import time

from backend.wallet.wallet import Wallet

BASE_PORT = 5000

BASE_URL = f'http://localhost:{BASE_PORT}'


def get_blockchain():
    return requests.get(f'{BASE_URL}/blockchain').json()


def get_blockchain_mine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()


def post_wallet_transact(recipient, amount):
    return requests.post(
        f'{BASE_URL}/wallet/transact',
        json={'recipient': recipient, 'amount': amount}
    ).json()


def get_wallet_info():
    return requests.get(f'{BASE_URL}/wallet/info').json()


start_blockchain = get_blockchain()
print(f'start_blockchain: {start_blockchain}')


radom_amount = random.randint(10, 20)
recipient = Wallet().address
post_wallet_transact_1 = post_wallet_transact(recipient, radom_amount)

print(f'\n\n-----\n\npost_wallet_transact_1: {post_wallet_transact_1}')

time.sleep(1)

radom_amount = random.randint(30, 40)
post_wallet_transact_2 = post_wallet_transact(recipient, radom_amount)

print(f'\n\n-----\n\npost_wallet_transact_2: {post_wallet_transact_2}')


time.sleep(1)

mined_block = get_blockchain_mine()

print(f'\n\n-----\n\nmined_block: {mined_block}')


wallet_info = get_wallet_info()

print(f'\n\n-----\n\nwallet_info: {wallet_info}')
