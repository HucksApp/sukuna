### SUKUNA🦍
![sukuna](https://github.com/HucksApp/sukuna/assets/58187974/bff5d76a-2b6e-4ee4-9e07-222847e35d52)


## Description ##
* Mnemonic wallet Bruteforcer using all available cpu core
* < removed 'transaction hijacker and double spend redirect'> 🏗
 
## The Bruteforcer ##  
* Creates crypto currency  wallet *Mnemonic* recovery phrases of specified length *(wallet strength)*.
* Creates hdd wallet of specifiesd cryto currency type <COIN_TYPE> from this recovery phrases 
* validates its balance on blockchain and writes the result if balance is greater than a range

## Usage ##
***The object classes could be used individually e.g wallet generation***

# cmd #
You must have python3 installed
```
 $ pip3 install pipenv
 $ pipenv install
```
OR
```
$ cd <path/to>/sukuna
$ ./install.sh
```
when already in project folder 
`$ ./start.py`

# file #
the start file has this fields

Fields              |            Description
--------------------|-------------------------
 ITERATION_NUMBER   | number of wallet to be created and  checked by each processor [ -i "value"]
 WALLET_STD         | Wallet standard or strength l.e number of words in recovery phrase 12, 15, 18, 21, 24  [ -s "value"]
 COIN_TYPE          | crypto currency type  [ -c "value" ]

**example**
`$ ./start.py -i 5000 -c btc -s 12`

# result #
The full wallet details along with the recovery phrase and balance is written in ***result.txt***
if balance > 0 . 

> ⚠️ 🔞  ❌
> This hack sofware is a test of the effectiveness of ***mnemonic phrase*** of mnemonic wallets.
>>**It is not intended to be exploited** ❗️❗️❗️

## Authors
Abiodun Aremu ~ HucksApp@gmail.com : 🖋
