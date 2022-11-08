from cryptic import start_brute_force


ITERATION_NUMBER=3000      # Any amount

WALLET_STD=12         # Wallet strenght ! 12 15 18 21 24


COIN_TYPE="btc"   #btc  eth  doge 



if __name__ == '__main__': 

    try:
        start_brute_force(ITERATION_NUMBER,WALLET_STD,COIN_TYPE)
    except Exception as e:
        print( e )



