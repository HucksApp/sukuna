# SUKUNA🦍
![sukuna](https://github.com/HucksApp/sukuna/assets/58187974/bff5d76a-2b6e-4ee4-9e07-222847e35d52)

## What Are Mnemonics? 

Mnemonics are simply songs 🎶 , abbreviations and rhymes that assist in remembering something.

In the world of cryptocurrencies, mnemonics is a group of words, usually 12 or more that are generated when a new crypto wallet is created.
The whole point of this is to ensure crypto wallets can be accessed if the password is lost.
It is very difficult to retrieve the details of a cryptocurrency wallet given its decentralized and secure nature.
But mnemonic groups can be used to retrieve details.

There are two types of mnemonics used in cryptocurrencies. These include the mnemonic phrase and mnemonic passphrase.

A mnemonic phrase is also called seed key 🔑, mnemonic seed, and recovery seed, to name a few abbreviations.
Every time a new crypto wallet is generated, users are encouraged to take note of a mnemonic phrase — 12, 18 or 24 words long — on a piece of paper or to store it in any other safe place.This ensures that users are not locked out of crypto wallets 💰. 
There are many obvious benefits of using a mnemonic phrase, including making the crypto wallet more secure and making it easier to store.

Mnemonic passphrases are an extra added layer of security, building up on mnemonic phrases, and act as a two-factor authentication for the crypto wallet.
They're also known as a mnemonic extension or a seed extension.

## BIP39 Wallet 💰
Bitcoin Improvement Proposals or BIP's are design features, inputs, ideas, information, or changes for essentially how Bitcoin works (including storage i.e. wallets).

One of these features is BIP39 (short for Bitcoin Improvement Proposal: 39). BIP39 is a standard that proposed utilizing a mnemonic phrase -- a group of easy to remember words -- to serve as a back up to recover your wallet and coins in the event your wallet becomes lost or destroyed. 


## BIP39 Word List 🔡
The words in your mnemonic phrase aren't just any random words. They are pulled from a ***specific list of 2048 words known as the BIP39 wordlist***. Upon start up, wallets that utilize the BIP39 standard will provide you a 12-24 word phrase randomly chosen from the standard BIP39 wordlist.

In this list, the first 4 letters are unique to each word.
To clarify “unique”, we mean literally the first 4 letters (not the first 4 different letters). For example the word “apple”, “appl” does not come up anywhere else in the BIP39 wordlist.
For words that only have 3 letters, there is no 4th letter. For example with the word “add”, there are no more letters afterwards and thus must be the word "add". The word “addict” is in the BIP39 wordlist but you would have used “addi” for “addict”.

In other words, there are no two words in this list with the same first 4 characters.
That means if you have the first 4 letters, you know the rest of the word by looking for those first 4 letters in the BIP39 wordlist. Some wallets will even fill in the rest of the word once the first 4 letters are entered. 

BIP39 Wallet Recovery 
Your coins are not stored on your wallet device. They're stored on the blockchain (i.e. a universal network) and can be accessed by utilizing your seed phrase. Your wallet stores the "access" to those coins, not the coins themselves.

If you are recovering an existing wallet, the wallet's software will ask you if you have an existing phrase or have the option to import one. You'll enter in your existing mnemonic seed phrase, and  your coins are recovered.


## Description 📖
* Mnemonic wallet Bruteforcer using all available cpu core
* < removed 'transaction hijacker and double spend redirect'> 🏗
 
## The Bruteforcer 💪🏽
* Creates crypto currency  wallet *Mnemonic* recovery phrases of specified length *(wallet strength)*.
* Creates hdd wallet of specifiesd cryto currency type <COIN_TYPE> from this recovery phrases 
* validates its balance on blockchain and writes the result if balance is greater than a range

> Blocks 🚫
>> This Bruteforcer do not account for the use of ***passphrase*** (added security).

## Classes 🆑
1. [Mnemonic](./crypto_spam/objects/mnemonics.py): Generate and validate Mnemonic Recovery phrase used by BIP39 wallets.
2. [Wallet](./crypto_spam/objects/wallet.py) : Creates Cryptocurency Hierarchical Deterministic wallet's  from Mnemonic recovery phrases

## Usage 🛠
***The object classes could be used individually e.g wallet generation***

# cmd #
Clone repository 📁🖥 ⇠ ⇠ 🌏📁
```
$ git clone https://github.com/HucksApp/sukuna/tree/main
```


You must have python3 installed
```
 $ cd <path/to>/sukuna/crypto_spam
 $ pip3 install pipenv
 $ pipenv install
```
OR
```
$ cd <path/to>/sukuna/crypto_spam
$ ./install.sh
```
when already in project folder 
`$ ./start.py`

# file 📄
the start file has this fields

Fields              |            Description
--------------------|-------------------------
 ITERATION_NUMBER   | number of wallet to be created and  checked by each processor [ -i "value"]
 WALLET_STD         | Wallet standard or strength l.e number of words in recovery phrase 12, 15, 18, 21, 24  [ -s "value"]
 COIN_TYPE          | crypto currency type  [ -c "value" ]

**example**
`$ ./start.py -i 5000 -c btc -s 12`

# result 📄
The full wallet details along with the recovery phrase and balance is written in ***result.txt***
if balance > 0 . 

> ⚠️ 🔞  ❌
> This hack sofware is a test of the collision of BIP39 Fixed ***list of 2048 mnemonic words*** in BIP39 mnemonic wallets.
>>**It is not intended to be exploited** ❗️❗️❗️

## Bugs 🐛 🪲
No known bugs at this time. 

## Authors 🖌
Aremu Mohammad Abiodun ~ [Github](https://github.com/Hucksapp) / [Twitter](https://twitter.com/hucks_jake)  

## License ©
Public Domain. No copy write protection. 

