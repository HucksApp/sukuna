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

sample.
```
(crypto_spam) ➜  crypto_spam git:(main) ./start -i 30 -c btc -s 12

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

# sample of a Wallet dump. for the btc sample shown, to be written in result, if balance is at specified range.
```
{'cryptocurrency': 'Bitcoin', 'symbol': 'BTC', 'network': 'mainnet', 'strength': 128,
'entropy': '7e64776a7c77417689cb7fe4247fcc5b', 'mnemonic': 'lazy casual surround wedding inject robust cheese husband tomorrow catalog vessel render',
'language': 'english', 'passphrase': None, 'seed':
'ed8be523916625fe4cfebda492f39fb7bb94f6d500ca20a40cb8b734283214b6145d280df880492d8953701cdaec80d236730b2b821f54653d29293faa4e4bd0', 'root_xprivate_key':
'xprv9s21ZrQH143K27Jds87ZFY1Th8VPmriAQhLQQwMxdqTYa85RvcWSxKuRsCJ4csq3NjD2DdYncNaWn2ADyRSD7AGw93saiWsK5DkjBfGYGUL', 'root_xpublic_key':
'xpub661MyMwAqRbcEbP6y9eZcfxCFAKtBKS1mvG1DKmaCAzXSvQaU9phW8DuiToL3o9asw3v5KWz4Pmqr4xbFBNV2maHNuzVJVCrNQt5UPLHeZN', 'xprivate_key':
'xprvA2ozv2XdviZ2ejdjaWHr6wq5QnHwwB6o6cW4WYdz7akGRnvuDYugKvXBNKDKJ6rbjrLVspkWmuwnfRs1PRXArbyXKuTVUFovqTpB2Kawro6', 'xpublic_key':
'xpub6FoMKY4Xm67KsDiCgXprU5moxp8SLdpeTqRfJw3bfvHFJbG3m6DvsiqfDctW6uiSpaammUWbhzyXGkw71pPpeKNnkn3m13W1bpmHBksVcrb', 'uncompressed':
'b87154f61a3dc19230b9b07adb86b64f34592ac486fb5f92ea674fd109819481a1ef940ae86626f9b0a62426129282f5a8be3e1174f50419cc86fc9a7801001b', 'compressed':
'03b87154f61a3dc19230b9b07adb86b64f34592ac486fb5f92ea674fd109819481', 'chain_code': 'e5580fdc86af040b99d6f1438209d5588b415e18c2af7212748d541d5e0480ad',
'private_key': '5c1568b7ca8bba1e1364aa8739cdd88425def84790232b6858270ac0a8c1b6a7', 'public_key':
'03b87154f61a3dc19230b9b07adb86b64f34592ac486fb5f92ea674fd109819481', 'wif': 'KzJi6kfBmnHWDGsgkMnMm5UrQuVDcjPR6cxMNVmfCxQsySPvd6wS', 'finger_print':
'd5021048', 'semantic': 'p2pkh', 'path': "m/44'/0'/0'/0/0", 'hash': 'd5021048955d4335b02da6945b9c82c8a01967c9', 'addresses': {'p2pkh':
'1LRHQF2ZnaqRfno92SSnhBLeou9DyK7fg2', 'p2sh': '3PPBzkXya5rU5QqG9xHTwJr7QKhRmTyQKD', 'p2wpkh': 'bc1q65ppqjy4t4pntvpd5629h8yzezspje7fjdsc8d', 'p2wpkh_in_p2sh':
'3MTSFqrgcRV1LSwaRotXfbsM91MACVwkBi', 'p2wsh': 'bc1qf5grd0ppnamwe3m4derrhnyw4tvp95f7uvwd7e0v6eddqvf7umwsxt5tk7', 'p2wsh_in_p2sh':
'3MLNzaK1dc3Fzk3bXE8t3L6b5Ufzq2VFgv'}}
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

