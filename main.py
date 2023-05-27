# from cosmpy.aerial.client import LedgerClient, NetworkConfig

# # connect to Fetch.ai network using default parameters
# ledger_client = LedgerClient(NetworkConfig.fetchai_mainnet())

# # alice: str = 'fetch12q5gw9l9d0yyq2th77x6pjsesczpsly8h5089x'
# alice: str = 'fetch168gv026mqmnt0hr4hsw7qr080f3m3dyranwt5e'
# balances = ledger_client.query_bank_all_balances(alice)


# # show all coin balances
# print( balances)
# # for coin in balances:
# #   print(f'{coin.amount}{coin.denom}')

from web3 import Web3

# Подключение к узлу блокчейна Ethereum (локальный узел или удаленный узел Infura)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bcfc6cf29c004d6aa0ca5110da8f521f'))

# Адрес кошелька, информацию о котором вы хотите получить
wallet_address = '0x96675ea0b9478751c79896b404474598dd693df5'

# Получение баланса кошелька
balance = w3.to_checksum_address(wallet_address)
# balance_in_eth = w3.from_wei(balance, 'ether')

# print(f'Баланс кошелька {wallet_address}: {balance_in_eth} ETH')
print(w3.to_wei(balance, "ether"))