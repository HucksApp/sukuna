import json
import os,random,binascii,hashlib
from pathlib import Path
from typing import Optional

from multiprocessing import Process,cpu_count

from hdwallet import HDWallet
from hdwallet.symbols import BTC,ETH,DOGE,SDC,XDC
from moneywagon import get_address_balance
#from moneywagon.services import BlockchainInfo, Toshi



from tqdm import tqdm



from mnemonics import MNEMONICS,WORD_GP




class Mnemonic :

    def __init__(self, word_strenght ) -> None:
        self._NUM_LIST:list[int]=[]
        self.mnemonic =""
        if word_strenght in WORD_GP:
            self._WORD_GP:int = word_strenght
        else:
            print("WRONG MNEMONIC CORE LENGTH")
            exit()
        
        self.ent:int= self.__enthropy_check(word_strenght)
        self.enthropy:str = self.__create_enthropy()
        self.enthropy.strip()
        self.__gen_enhropy_wchecksum()
        self.__generate_mnemonic()



    


    def __enthropy_check(self,word_size:int )-> dict[str, int]:
        MS = word_size*11 ## mnemoic sentence resulting length
        F_ENT = MS          ## final entropy length (enthropy + checksum)
        CS = F_ENT//32 #checksum Lenght
        ENT = F_ENT-CS         #initial enthropy length
        return {
                "MS":MS,
                "CS":CS,
                "ENT":ENT,
                "F_ENT":F_ENT
                }

    ###############from binary bits string return decimal no in base 10
################after spliting in step->11
    def decimal_index(self,bina:str, step:int) ->list[str]:
        bin_list:list[str]=[bina[i:i+step] for i in range(0, len(bina), step)]
        dec_list:list[int]=[]
        for n in bin_list:
            dec_list.append(int(n,2))
        return dec_list
    
    



    def __create_enthropy(self)-> None:
        for n in range(self.ent['ENT']):
            self._NUM_LIST.append(random.randint(0,1))  
        return "".join(str(bi)for bi in self._NUM_LIST)




    def __gen_enhropy_wchecksum(self)->None:

        #hexstr = "{0:0>4X}".format(int(self.enthropy,2))
        #hexstr =f'{int(self.enthropy, 2):X}'

        hexstr ='%0*X' % ((len(self.enthropy) + 3) // 4, int(self.enthropy, 2))
        #print(f'hex-----> {hexstr} lenght {len(hexstr)}\n')
        #print(f'full enthropy lenght -----> {len(self.enthropy)}\n')
        data = binascii.a2b_hex(hexstr) 

        sha_cryp= hashlib.sha256(data )
        self.sha_cryp:str = sha_cryp.hexdigest()
        checksum_hex=self.sha_cryp[:2]

        checksum_bin:str=bin(int(checksum_hex, 16))[2:].zfill(8)
        check_sum:str=checksum_bin[:(self.ent['CS'])]
        #print(check_sum,checksum_bin)
        self.raw_enthropy:str =self.enthropy
        self.enthropy +=check_sum

        #print(self.raw_enthropy)

        #VALIDATE FINAL ENTHROPY
        if len(self.enthropy) != self.ent["F_ENT"]:
            print("bad string generated")
            exit()




    def __generate_mnemonic(self):
        mnemonic_rxt:list[str] =[]
        dec_index= self.decimal_index(self.enthropy, 11)
        
        for no in  dec_index:
            mnemonic_rxt.append(MNEMONICS[no])

        #print(sha_cryp,raw_enthropy,len(raw_enthropy),len(enthropy),mnemonic_rxt,enthropy)
        self.mnemonic = "".join(word+" " for word in mnemonic_rxt).strip()




#use on mnemonic text file
    def mnemonicsf_reader(self,file_n:str)->tuple[str,...]:
        f_path= os.path.dirname(__file__)+"/" +file_n
        mnemonics:list[str]=[]
        with open(f_path, "r") as f:
            for word in f:
                #print(word)
                mnemonics.append(word.strip())
        return tuple(mnemonics)


   








class Wallet (Mnemonic):


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

    
    def wallet_balance(self, address) -> float:
        self.balance:float = get_address_balance(self.coin_type, address, random=False)
        return self.balance






    def write(self,file_n:str )->None:
        f_path= os.path.dirname(__file__)+"/" +file_n
        data = f'MNEMONICS:{self.mnemonic}\n BALANCE:{self.balance}\nINITIAL_ENTHROPY:{self.raw_enthropy}\nFINAL_ENTHROPY:{self.enthropy}\n WALLET DETAILS:{json.dumps(self.dump)} \n\n\n\n'
        with open(f_path, "a") as f:
            f.write(data)


        




#FUNCTION TO START THE BRUTEFORCER 
# USING ALL AVAILABLE CPU PROCESSOR
def start_brute_force(iter:int,wallet_std:int,coin_type:str)-> None:
    count:int=0
    result:int=0
    c=cpu_count()
    print(f"\n  ******BRUTEFORCING FOR {iter } * WITH {c} PROCESSORS. SCANNING TOTAL POSSIBLE {iter * c} FOR {coin_type} WALLETS**********  \n")
    
    for cpu in range(cpu_count()):
        Process(target=__run, args=(iter,count, result,wallet_std,coin_type)).start()



def  __run(iter:int,count:int,result:int,wallet_std:int,coin_type:str)->None:
        for i in tqdm(range(iter)):
            #time.sleep(0.1)
            wallet = Wallet(wallet_std,coin_type)
            count+=1
            if float(wallet.balance) > 0.0:
                result+=1 
                print(wallet.balance, wallet.dump)
                wallet.write('result.txt')
        print(f'\n GOT {result} of {count} WALLETS CHECKED\n')




