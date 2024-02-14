from http.client import responses
import os, time
from typing import Dict
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.remote.webelement import WebElement


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_option
from selenium.webdriver.firefox.options import Options  as firefox_option
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from fp.fp import FreeProxy
from reader import write




data={"last_name":"bahk", "dob":"02/21/1982", "ssn":359899952}




f_path= os.path.dirname(__file__)

chrome_path =f'{f_path}/selenium/chromedriver'
firefox_path = f'{f_path}/selenium/geckodriver'

options = chrome_option()
#options = firefox_option()
#profile = webdriver.FirefoxProfile()

proxy = FreeProxy(country_id=['US']).get()
PROXY =proxy.split("//")[1]
#PROXY='165.227.79.99:7497'
print(f'using proxy server: {proxy.split("//")[1]}')

chrome_dev_bin="/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome Dev"
#firefox_dev_bin='/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox-bin'

options.add_argument('--proxy-server=%s' % PROXY)

#options.set_preference('profile', profile_path)
#options.set_preference('profile', firefox_dev_bin)
#options.set_preference('network.proxy.type', 1)
#options.set_preference('network.proxy.socks', PROXY.split(":")[0])
#options.set_preference('network.proxy.socks_port', int(PROXY.split(":")[1]))
#options.set_preference('network.proxy.socks_remote_dns', False)

options.binary_location=chrome_dev_bin
#options.binary_location=firefox_dev_bin

#driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox(firefox_path)






#driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(options=options, executable_path=chrome_path)






def clear(element:WebElement)->None:
    for i in element.get_attribute("value"):
        element.send_keys(Keys.BACK_SPACE)





def ally_enroll(datas:list[dict], url:str):
    page = driver.get(url)

    try:
        #create_prof = driver.find_element(By.CSS_SELECTOR,"p.'sc-fmlJLJ cYgoBX' a.'sc-cVkrFx jfTFmT'")
        #create_prof= driver.find_element(By.LINK_TEXT,"Create a profile")

        session=False
        count = 1
        for data in datas:
            if  session== False:
                create_prof = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.LINK_TEXT,"Create a profile")))
                print(create_prof)
                create_prof.click()


                #form =driver.find_element(By.CSS_SELECTOR,"form#enroll-customer-form")

                last_name =WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input#lastName.sc-iWFSnp.czjHdw.sc-jLiVlK.sc-cHjxUU.dAXayC")))

                #last_name = driver.find_element(By.CSS_SELECTOR,"input#lastName.sc-iWFSnp.czjHdw.sc-jLiVlK.sc-cHjxUU.dAXayC")
                dob= driver.find_element(By.CSS_SELECTOR,"input#dateOfBirth")
                ssn = driver.find_element(By.CSS_SELECTOR,"input#ssn")
                submit =driver.find_element(By.CSS_SELECTOR,"button.sc-httYMd")
                session=True

            
            try:

                last_name.send_keys(data["last_name"])
                dob.send_keys(data["date of birth"])
                ssn.send_keys(data["ssn"])
                submit.submit()


                no_acct ="We can't find a user with that information. Double-check that all fields are entered correctly."
                enrolled="You already have a username and password on file with us. If you remember your username, please log in below. If you've forgotten your username, please call us at 1-877-247-2559 (ALLY). We're here 24/7 to help."
                time.sleep(10)
               

                modal =WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,"p.sc-fmlJLJ.fnQlCR.sc-eFubAy")))
                if modal and modal.text== enrolled:
                    print("used", count)
                    close_modal =driver.find_element(By.CSS_SELECTOR,"button.sc-gYhigD")
                    close_modal.click()
                    clear(last_name)
                    clear(dob)
                    clear(ssn)
                
            except Exception as e:
                try:
                    feed_back = driver.find_element(By.CSS_SELECTOR,"b.sc-fmlJLJ")
                    if feed_back and feed_back.text == no_acct:
                    
                        #sc-fmlJLJ fnQlCR  sc-eFubAy eNDnSb
                        print("no account", count) 
                        clear(last_name)
                        clear(dob)
                        clear(ssn)
                    elif feed_back and feed_back.text == "":
                        pass

                    else:           # if element is present and value is not equal to feed_back
                        print(data,"01")
                        write(data)
                        driver.back()
                except Exception as e: # if element do not exists 
                    #print(data, "02")
                    #write(data)
                    driver.close()

            count +=1
                




    except Exception as e:
        print(e, "03")
        print("-------> ---------> ----------->last exe")
        driver.back()
        session=False



    #print(driver.title)

    time.sleep(15)




