import time
from multiprocessing import Process,cpu_count
from tqdm import tqdm
from objects.wallet import Wallet




def start_brute_force(iter:int,wallet_std:int,coin_type:str)-> None:
    """
        MNEMONICS HDD WALLET BRUTEFORCER
        USING ALL AVAILABLE CPU PROCESSOR
    """
    count:int=0
    result:int=0
    c=cpu_count()
    print(f"\n       Bruteforcing {iter * c} {coin_type} Wallets for Balance Greater than Zero")
    print(f"----------------------------------------------------------------------------------------")
    print(f'[+]    Using {c} numbers of Processors to  check {iter} wallet')
    print(f'[*]    <numbers of Processors> * <iteration>')
    print(f'[*]    Searching {iter * c} {coin_type} wallet')
    print(f'[-*]',end="")

    for cpu in range(cpu_count()):
        Process(target=__run, args=(iter,count, result,wallet_std,coin_type)).start()



def  __run(iter:int,count:int,result:int,wallet_std:int,coin_type:str)->None:
        """
            starter function for the wallet bruteforcer
        """
        for i in tqdm(range(iter)):
            wallet = Wallet(wallet_std,coin_type)
            count+=1  
            if float(wallet.balance) > 0.0:
                result+=1 
                print(wallet.balance, wallet.dump)
                wallet.write('result.txt')
            # slowdow Brutefore not to trigger throttle
            if count%2==0:
                time.sleep(25)
            #-----------------------------
        print(f'\n GOT {result} of {count} WALLETS CHECKED\n')

