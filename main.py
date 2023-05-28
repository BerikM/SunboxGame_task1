from web3 import Web3

# Подключение к локальному узлу Ethereum
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
account = ''
#private key
#0xd0d83c4aa1223f4207d7bb170480f9525a11f63e44d509b1fd42acd2b565810a
recipient = ''
# Получение баланса кошелька
def getBalance(account):
    return w3.eth.get_balance(account.address)
#recipient
#'0x2AFe86947ce7EB9C0e031968e0aC2681fF832b10'  # Адрес получателя
def checkValidKey(key):
    try:
        account = w3.eth.account.from_key(private_key)
        print("account accepted")
        return account
    except:
        print("not correct key")
        return ''
    
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
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=account.key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'hash of transaction: {w3.to_hex(tx_hash)}')
    except:
       print("you do not have enough funds for the transaction or do not have access")
print("Use 'help' for information")
while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    elif command == "help":
        print("user -key 'key' ---- to set user key")
        print("send 'address' 'amount' ---- for send eth on wallet use ")
        print("balance ---- or check balance on you wallet use ")
        print("exit ---- close programm")
    elif command.startswith("user -key"):
        parts = command.split(" ")
        private_key = parts[2]
        account = checkValidKey(private_key)
    elif command.startswith("send"):
        parts = command.split(" ")
        try:
            address = parts[1]
            amount = parts[2]
            if(account != ""):
                transaction = transaction_info(address, amount, account)
                transaction_block(account, transaction)
            else:
                print("before use command user -key 'your private key'")
        except:
            print("dont entered address or amount")
    elif command == "balance":
        if(account != ""):
            print(getBalance(account), "wei")
        else:
            print("before use command user -key 'your private key'")
    else:
        print("undefined command. Use -help")