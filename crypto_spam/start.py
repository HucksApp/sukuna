#!/usr/bin/env pipenv run python3
from runner import start_brute_force
from sys import argv
"""
The Bruteforcer attempts
    create mnemonic wallet phrases depending on <Wallet strenght>
    create hdd wallet of type <COIN_TYPE>
    verify the wallet ballance 
    write the total wallet information along with mnemonic
        recovery phrase if balance is greater than zero
"""

ITERATION_NUMBER=6000      # Any amount

WALLET_STD=24         # Wallet strenght ! 12 15 18 21 24

COIN_TYPE="eth"   #btc  eth  doge 


if len(argv) > 1:
    for  i in range(1, len(argv) - 1):
        if argv[i] == "-i":
            ITERATION_NUMBER = int(argv[i + 1])
        if argv[i] == "-c":
            COIN_TYPE = argv[i + 1]
        if argv[i] == "-s":
            WALLET_STD = int(argv[i + 1])

if __name__ == '__main__': 
    try:
        start_brute_force(ITERATION_NUMBER,WALLET_STD,COIN_TYPE)
    except Exception as e:
        print( e )
