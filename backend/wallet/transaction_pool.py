import re


class TransactionPool:
    def __init__(self):
        self.transaction_map = {}

    def set_transaction(self, transaction):
        """
        Set a transaction in the transaction pool.
        """
        self.transaction_map[transaction.id] = transaction

    def existing_transaction(self, address):
        """
        Find a transaction from the transaction pool for an address.
        """
        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction

    def transaction_data(self):
        """
        Return the transaction data of the pool.
        json format.
        """
        transaction_values = self.transaction_map.values()

        transaction_data = list(
            map(lambda transaction: transaction.to_json(), transaction_values))

        return transaction_data
