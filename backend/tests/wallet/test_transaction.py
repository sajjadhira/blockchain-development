
import pytest
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
