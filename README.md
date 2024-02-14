### mnemonic wallet Brute forcer using all available cpu core ### 
 
## This Bruteforcer ##  
* Creates crypto currency  wallet *Mnemonic* recovery phrases of specified length *(wallet strength)*.
* Creates hdd wallet of specifiesd cryto currency type <COIN_TYPE> from this recovery phrases 
* validates its balance on blockchain and writes the result if balance is greater than a range

## Usage ##
# cmd #
You must have python3 installed
`$ pip3 install pipenv`
`$ pipenv install`
OR
`cd <path/to>/sukuna`
`./install.sh`
when already in project folder 
`$ ./start`

# file #
the start file has this fields

Fields              |            Description
--------------------|-------------------------
 ITERATION_NUMBER   | number of wallet to be created and  checked by each processor
 WALLET_STD         | Wallet standard or strength l.e number of recovery words in phrase 12, 15, 18, 21, 24
 COIN_TYPE          | crypto currency type


# result #
The full wallet details along with the recovery phrase and balance is written in ***result.txt***
if balance > 0 . 
