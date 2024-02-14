import os,random,binascii,hashlib
from utils import MNEMONICS,WORD_GP





class Mnemonic :

    def __init__(self, word_strenght:int ) -> None:
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
        data = binascii.a2b_hex(hexstr) 
        sha_cryp= hashlib.sha256(data )
        self.sha_cryp:str = sha_cryp.hexdigest()
        checksum_hex=self.sha_cryp[:2]
        checksum_bin:str=bin(int(checksum_hex, 16))[2:].zfill(8)
        check_sum:str=checksum_bin[:(self.ent['CS'])]
        self.raw_enthropy:str =self.enthropy
        self.enthropy +=check_sum

        if len(self.enthropy) != self.ent["F_ENT"]:
            print("bad string generated")
            exit()

    def __generate_mnemonic(self):
        mnemonic_rxt:list[str] =[]
        dec_index= self.decimal_index(self.enthropy, 11)
        for no in  dec_index:
            mnemonic_rxt.append(MNEMONICS[no])

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

