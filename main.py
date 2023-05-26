from cosmos_sdk.client.lcd import LCDClient
from cosmos_sdk.key.mnemonic import MnemonicKey
import cobra

mnemonic = <MNEMONIC_PHRASE>

# Terra client
terra_client = LCDClient(chain_id="phoenix-1", url="https://phoenix-lcd.terra.dev")
mk = MnemonicKey(mnemonic,"terra")
terra_wallet = terra_client.wallet(mk)

