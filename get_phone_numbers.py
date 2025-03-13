from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json
username = "guruvak@dopagent.com"
passw = "jssj"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.dopagentsoftware.com/admin/index")
driver.maximize_window()
sigh_in_u = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div[1]/input')
sigh_in_u.send_keys(username)
sigh_in_p = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div[2]/input')
sigh_in_p.send_keys(passw)
login_btn = driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div[3]/input')
login_btn.click()

driver.get('https://www.dopagentsoftware.com/admin/users/super/?limit=all&user_type=super&plan_type=all&callback_from=&callback_to=&expiry_from=&expiry_to=&search=&phone=&city=&status=A&demo_status=ALL&payment_year=no&payment_month=no&states%5B%5D=AR&states%5B%5D=AS&states%5B%5D=BR&states%5B%5D=CT&states%5B%5D=GA&states%5B%5D=GJ&states%5B%5D=HR&states%5B%5D=HP&states%5B%5D=JK&states%5B%5D=JH&states%5B%5D=MP&states%5B%5D=MH&states%5B%5D=MN&states%5B%5D=ML&states%5B%5D=MZ&states%5B%5D=NL&states%5B%5D=OR&states%5B%5D=PB&states%5B%5D=RJ&states%5B%5D=SK&states%5B%5D=TR&states%5B%5D=UK&states%5B%5D=UP&states%5B%5D=WB&states%5B%5D=AN&states%5B%5D=CH&states%5B%5D=DN&states%5B%5D=DD&states%5B%5D=DL&states%5B%5D=LD&states%5B%5D=PY&exe_version=&submit=submit')

phone_dict = {}
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
for row in rows:
    identifier = row.find_element(By.XPATH, "./td[2]").text.strip()  
    phone_text = row.find_element(By.XPATH, "./td[3]").text.strip()

    phone_text = phone_text.replace('\n', ',')

    phone_list = phone_text.split(',')
    if phone_list:
        phone_dict[phone_list[0].strip()] = {'status': False, 'name': identifier}
        
with open('data.json', 'w') as json_file:
    json.dump(phone_dict, json_file, indent=4)

print("JSON file created successfully.")
print("done")

driver.quit()