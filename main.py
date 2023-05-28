from web3 import Web3

# Подключение к локальному узлу Ethereum
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# подключение кошелька
private_key = "0xd0d83c4aa1223f4207d7bb170480f9525a11f63e44d509b1fd42acd2b565810a"
account = w3.eth.account.from_key(private_key)

# Получение баланса кошелька
balance = w3.eth.get_balance(account.address)
print(f'Баланс кошелька: {balance} wei')

# Отправка транзакции
recipient = '0x2AFe86947ce7EB9C0e031968e0aC2681fF832b10'  # Адрес получателя
amount = 1  # Количество эфира для отправки

# Подготовка транзакции

def transaction_info(recipient, amount, account):
    return {
    'to': recipient,
    'value': w3.to_wei(amount, 'ether'),
    'gas': 21000,
    'gasPrice': w3.to_wei('50', 'gwei'),
    'nonce': w3.eth.get_transaction_count(account.address),

}

def transaction_block(account, transaction):
    try:
        # Подпись транзакции
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=account.key)

        # Отправка подписанной транзакции
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Хэш транзакции: {w3.to_hex(tx_hash)}')
    except:
       print("you do not have enough funds for the transaction or do not have access")

transaction = transaction_info(recipient, amount, account)
transaction_block(account, transaction)