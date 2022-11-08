from ally_spam import  ally_enroll
from reader import reader







sort_keys="Name,Date of birth,Age,Gender,Height Feet,Height Inch,Weight,SSN,Occupation,Address,City,State,Zip Code,Country,Home Phone,Work Phone,Email,Selected Plan,Type,payment Mode,Policy,Payment Option,Agent Name,Signed Date,Status,Status Date,Application Effective Date"
seperator = ","
fullz_file = 'fullz.txt'





fullz_list = reader(fullz_file,sort_keys,seperator)
ally_enroll(fullz_list)
