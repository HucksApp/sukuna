import os
from typing import List, Union






def write( data:dict[str,str])->None:
    f_path= os.path.dirname(__file__)+"/resources/result.txt"
    with open(f_path, "a") as f:
        rxt:str=""
        for key, value in data.items():
            rxt += f'{key} : {value}\n'
        f.write("\n\n"+ rxt.strip()+ "\n\n")











def reader(file_n:str,sort_keys:str, seperator:str, names=True)->list[dict]:
    targ_list:list[dict]=[]
    name_index:int =0
    if names :
        sort_keys:Union[str,list[str]]=sort_keys.lower()

        sam_list:list[str] =sort_keys.split(seperator)
        name_index = sam_list.index("name")
        sam_list.pop(name_index)
        sam_list.insert(name_index,"first_name")
        sam_list.insert(name_index+1,"middle_name")
        sam_list.insert(name_index +2, "last_name")
        sort_keys = sam_list

    f_path= os.path.dirname(__file__)+"/resources/" +file_n
    with open(f_path, "r") as f:
        for line in f:
            c_line = line.strip().split(seperator)
            if names :
                
                c_name = c_line[name_index].strip().split(" ")
                c_line.pop(name_index)

                last_name:str =c_name[2]
                mid_name:str = c_name[1]
                if len(c_name) > 3:
                    last_name:str = c_name[2] + " "+ c_name[3]
                elif len(c_name) ==2:
                    last_name:str = c_name[1]
                    mid_name:str = " "

                
                c_line.insert(name_index, c_name[0])
                c_line.insert(name_index+1, mid_name)
                c_line.insert(name_index+2, last_name)
                    

            sort_dict = dict(zip(sort_keys,c_line))
            #print(c_line)
            sort_dict['ssn']=sort_dict['ssn'].replace("-","")
            sort_dict["date of birth"]=sort_dict["date of birth"].replace("-","/")
            dob_cleaned =""
            for n in sort_dict["date of birth"].split("/"):
                if len(n)<2:
                    n = "0" + n
                    dob_cleaned += n+"/"
            if dob_cleaned != "":
                sort_dict["date of birth"] = dob_cleaned
            

            targ_list.append(sort_dict)
    return  targ_list
    

 

#sort_keys="Name,Date of birth,Age,Gender,Height Feet,Height Inch,Weight,SSN,Occupation,Address,City,State,Zip Code,Country,Home Phone,Work Phone,Email,Selected Plan,Type,payment Mode,Policy,Payment Option,Agent Name,Signed Date,Status,Status Date,Application Effective Date"
#seperator = ","
#fullz_file = 'fullz.txt'





#fullz_list = reader(fullz_file,sort_keys,seperator)
