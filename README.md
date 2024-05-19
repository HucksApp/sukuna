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
## Start Bruteforcer
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

sample.
```
(crypto_spam) ➜  crypto_spam git:(main) ./start.py -i 30 -c btc -s 12

       Bruteforcing 240 btc Wallets for Balance Greater than Zero
----------------------------------------------------------------------------------------
[+]    Using 8 numbers of Processors to  check 30 wallet
[*]    <numbers of Processors> * <iteration>
[*]    Searching 240 btc wallet
 83%|████████████████████████████████████████████████████████████            | 25/30 [05:28<00:56, 11.29s/it]
```


# result 📄
The full wallet details along with the recovery phrase and balance is written in ***result.txt***
if balance > 0 .

sample of a Wallet dump. for the btc sample shown, to be written in result, if balance is at specified range  ☝️
```
 MNEMONICS:slim evolve awkward circle gallery system hotel diamond fox machine wear suffer
 BALANCE: 1.2
 INITIAL_ENTHROPY: 11001011110010011100010001000011000101001001010111110001101110011001101110001001111010010101110001010000101100111110000111101100
 FINAL_ENTHROPY: 110010111100100111000100010000110001010010010101111100011011100110011011100010011110100101011100010100001011001111100001111011000101
 WALLET DETAILS:{
    "cryptocurrency": "Bitcoin",
    "symbol": "BTC",
    "network": "mainnet",
    "strength": 128,
    "entropy": "cbc9c4431495f1b99b89e95c50b3e1ec",
    "mnemonic": "slim evolve awkward circle gallery system hotel diamond fox machine wear suffer",
    "language": "english",
    "passphrase": null,
    "seed": "fff1c4d66ba9e7dc6ecf65e41baf615117ea17ce4c75cad52742167427dc59f3d4c64c253a8569b43c46b3784e52c00d2449500b70b113f1d148eed852708713",
    "root_xprivate_key": "xprv9s21ZrQH143K48AYtVfxT3Ej42tUFpcCxwsv1z8LR9SncnnDLN5qpXdbkbmfPqUHRoAJ8gfb7PKWTxGY5bB3tAiJkp74HW124ZTkbpUX9Cf",
    "root_xpublic_key": "xpub661MyMwAqRbcGcF1zXCxpBBTc4ixfHL4LAoWpNXwyUymVb7MsuQ6NKx5bsZ7NXaotiE3jcHuXWu54LNEBjnMzVGnWZ9csnBQvU4prdqoBvF",
    "xprivate_key": "xprvA31WNGtooLWcGEfVsnmhD1jYvRarzpNLBESwDkCDwhYMAb5YjCDW6NBaTAuuY3yppHpa39gXrNgmJMnB8AiAKfMf19GJHy4BgZ4SzPtp79p",
    "xpublic_key": "xpub6FzrmnRhdi4uUijxypJha9gHUTRMQH6BYTNY28bqW35L3PQhGjXkeAW4JRPxsg9ZjsYoVWyghUULMwHCM9xbykTRqBfT8YuggTUssWbthSf",
    "uncompressed": "132e2b6e6b8f3a515c729ad6503a508d99cdb69af5a1b8a33762de2ded1d4400b60209b96c019da4461f228a555aa02516503d7d7dd2894b858d50e0a7480190",
    "compressed": "02132e2b6e6b8f3a515c729ad6503a508d99cdb69af5a1b8a33762de2ded1d4400",
    "chain_code": "15dd76b7287dc5d6ded72894d2656c895f6201a6750e29a3d61fd9bb38119340",
    "private_key": "5b2dc5afc8e13371e5868ee74abd1b6043ab7445d3d3a6608cf9829a0351f719",
    "public_key": "02132e2b6e6b8f3a515c729ad6503a508d99cdb69af5a1b8a33762de2ded1d4400",
    "wif": "KzGx5uEM2h8czfVJeGaaq2vNbNNMpysRZJuejyt4ZtQNWewCe9YP",
    "finger_print": "474dcb27",
    "semantic": "p2pkh",
    "path": "m/44'/0'/0'/0/0",
    "hash": "474dcb275a6f2f2fb3cfaac67cf9ac0972aa89c6",
    "addresses": {
        "p2pkh": "17W2Ap6GHUtbT69JvYaFoh8WpuLHJUChC8",
        "p2sh": "37w2z55gUCL2JwLwjnnrP438fNwY9sB5ch",
        "p2wpkh": "bc1qgaxukf66duhjlv704tr8e7dvp9e24zwxnj7mah",
        "p2wpkh_in_p2sh": "3LyPCHLFPgRayKGqmgDStkVhKAXMwZtWoU",
        "p2wsh": "bc1q4evynl0tnm9ad0r68wvz8w4mtazh7vrdcv6yflappkexsvcek30q25rn03",
        "p2wsh_in_p2sh": "3BLrXFtThuot7b1Q1NMbHsFHjc2Z8o5b1i"
    }
} 

```

> ⚠️ 🔞  ❌
> This hack sofware is a test of the collision of BIP39 Fixed ***list of 2048 mnemonic words*** in BIP39 mnemonic wallets.
>>**It is not intended to be exploited** ❗️❗️❗️

## Bugs 🐛 🪲
No known bugs at this time. 

## Authors 🖌
Aremu Mohammad Abiodun ~ [Github](https://github.com/Hucksapp) / [Twitter](https://twitter.com/hucks_jake)  

## License ©
Public Domain. No copy write protection. 

