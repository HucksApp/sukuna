#!/usr/bin/env pipenv run python3
import json
import os
from typing import Optional
import objects.mnemonics  as a
from hdwallet import HDWallet
from hdwallet.symbols import BTC,ETH,DOGE,SDC,XDC
from moneywagon import get_address_balance






class Wallet (a.Mnemonic):


    def __init__(self, word_strenght,coin_type='btc',passphrase=None) -> None:
        super().__init__(word_strenght)
        wallet_dcoins:dict={"btc":BTC,"eth":ETH,"doge":DOGE,"sdc":SDC,"xdc":XDC}

        self.dump:dict[str ,str]={}
        self.PASSPHRASE: Optional[str]= passphrase
        self.__wallet_Coin_type(wallet_dcoins,coin_type)
        self.create_wallet()
        self.wallet_balance(self.dump['addresses']["p2pkh"])


    def __wallet_Coin_type (self, wallet_coins:dict,coin_type:str)->None:
        if coin_type.lower() in wallet_coins.keys():
            self.Wallet_coin = wallet_coins[coin_type.lower()]
            self.coin_type=coin_type.lower()



    def create_wallet(self)-> None:
        hdwallet:HDWallet = HDWallet(symbol=self.Wallet_coin, use_default_path=True)
       
        hdwallet.from_mnemonic(mnemonic=self.mnemonic, passphrase=self.PASSPHRASE)
        self.dump=hdwallet.dumps()
        # DIFFERENT USEABLE ADDRESS GENERATED CHECK WALLET DUMP FOR FULL  DETAILS
        #print(f'MNEMONICS: {self.mnemonic}\nCOIN: {self.Wallet_coin}\nP2PKH WALLET ADDRESS: { self.dump["addresses"]["p2pkh"] }\n')

    
    def wallet_balance(self, address:str) -> float:
        self.balance:float = get_address_balance(self.coin_type, address, random=False)
        return self.balance


    def write(self,file_n:str )->None:
        f_path= os.path.dirname(__file__)+"/" +file_n
        data = f'MNEMONICS:{self.mnemonic}\n BALANCE:{self.balance}\nINITIAL_ENTHROPY:{self.raw_enthropy}\nFINAL_ENTHROPY:{self.enthropy}\n WALLET DETAILS:{json.dumps(self.dump)} \n\n\n\n'
        with open(f_path, "a") as f:
            f.write(data)

