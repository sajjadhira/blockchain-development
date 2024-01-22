
from more_itertools import first
import pytest
from backend.config import MINING_REWARD, MINING_REWARD_INPUT, STARTING_BALANCE
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet


def test_transaction():
    wallet = Wallet()
    recipient = 'recipient'
    amount = 50
    transaction = Transaction(wallet, recipient, amount)

    assert transaction.output['recipient'] == amount
    assert transaction.output[wallet.address] == wallet.balance - amount

    assert 'timestamp' in transaction.input

    assert transaction.input['amount'] == wallet.balance
    assert transaction.input['address'] == wallet.address
    assert transaction.input['public_key'] == wallet.public_key
    assert Wallet.verify(
        transaction.input['public_key'],
        transaction.output,
        transaction.input['signature']
    )


def test_transaction_exceeds_balance():
    with pytest.raises(Exception, match='Amount exceeds balance'):
        Transaction(Wallet(), 'recipient', 9001)


def test_transaction_update_exceeds_balance():
    wallet = Wallet()
    transaction = Transaction(wallet, 'recipient', 50)

    with pytest.raises(Exception, match='Amount exceeds balance'):
        transaction.update(wallet, 'new_recipient', 9001)


def test_transaction_update():
    sender_wallet = Wallet()
    first_recipient = 'first_recipient'
    first_amount = 50
    transaction = Transaction(sender_wallet, first_recipient, first_amount)

    next_recipient = 'next_recipient'
    next_amount = 75
    transaction.update(sender_wallet, next_recipient, next_amount)

    assert transaction.output[next_recipient] == next_amount
    assert transaction.output[sender_wallet.address] == \
        sender_wallet.balance - first_amount - next_amount
    assert transaction.output[sender_wallet.address] == 875

    assert Wallet.verify(
        transaction.input['public_key'],
        transaction.output,
        transaction.input['signature']
    )

    to_first_again_amount = 25
    transaction.update(sender_wallet, first_recipient, to_first_again_amount)
    assert transaction.output[first_recipient] == \
        first_amount + to_first_again_amount

    assert Wallet.verify(
        transaction.input['public_key'],
        transaction.output,
        transaction.input['signature']
    )


def test_valid_trasaction():
    Transaction.is_valid_transaction(Transaction(Wallet(), 'recipient', 50))


def test_valid_trasaction_with_invalid_outputs():
    wallet = Wallet()
    transaction = Transaction(wallet, 'recipient', 50)
    transaction.output[wallet.address] = 9001

    with pytest.raises(Exception, match='Invalid transaction output values'):
        Transaction.is_valid_transaction(transaction)


def test_valid_trasaction_with_invalid_signature():
    transaction = Transaction(Wallet(), 'recipient', 50)
    transaction.input['signature'] = Wallet().sign(transaction.output)

    with pytest.raises(Exception, match='Invalid signature'):
        Transaction.is_valid_transaction(transaction)


def test_reward_transaction():
    miner_wallet = Wallet()
    transaction = Transaction.reward_transaction(miner_wallet)

    assert transaction.input == MINING_REWARD_INPUT
    assert transaction.output[miner_wallet.address] == MINING_REWARD
    # assert miner_wallet.balance == STARTING_BALANCE + MINING_REWARD


def test_valid_reward_transaction():
    reward_transaction = Transaction.reward_transaction(Wallet())
    Transaction.is_valid_transaction(reward_transaction)


def test_invalid_reward_transaction_extra_recipient():
    reward_transaction = Transaction.reward_transaction(Wallet())
    reward_transaction.output['extra_recipient'] = 60

    with pytest.raises(Exception, match='Invalid mining reward'):
        Transaction.is_valid_transaction(reward_transaction)


def test_invalid_reward_transaction_invalid_amount():
    miner_wallet = Wallet()
    reward_transaction = Transaction.reward_transaction(miner_wallet)
    reward_transaction.output[miner_wallet.address] = 9001

    with pytest.raises(Exception, match='Invalid mining reward'):
        Transaction.is_valid_transaction(reward_transaction)
