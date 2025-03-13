from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json,random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
with open('data.json') as file:
    data = json.load(file)

def save_json_file(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    
driver.get(f"https://web.whatsapp.com")
input("scan krooo: ")
time.sleep(10)



for phn in data:
    try:
        values = data[phn]
        status = values['status']
        
        number = phn
        name = values["name"]
        if data[phn]['status'] == False:
            message = f"""
            Hi {name},%0aWe are from Dop Agent Software.%0aHi {name}, हम Dop Agent Software से हैं।%0aहमारे व्हाट्सएप चैनल से जुड़ें! लिंक पर क्लिक करें:%0ahttps://whatsapp.com/channel/0029VakNRKXHbFVEGSFOic3p
            """
            driver.get(f"""https://web.whatsapp.com/send?phone={number}&text={message}""")
            wait = random.randint(5,10)
            time.sleep(wait)
            # driver.find_elements(by=By.CLASS_NAME,value=)
            element = driver.find_element(By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            
            element.click()
            data[phn]['status'] = True
            time.sleep(random.randint(2, 5))
            
    except:
        data[phn]['status'] = True
        save_json_file(data)
    
save_json_file(data)
    

# driver.quit()
# document.getElementsByClassName('x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf')[0].click()