import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from func import get_athlete_name

load_dotenv()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Opening Strava's login page
driver.get("https://strava.com/login")

time.sleep(2)

username = driver.find_element(By.ID, "email")
username.send_keys(os.getenv("USER_EMAIL"))
pword = driver.find_element(By.ID, "password")
pword.send_keys(os.getenv("USER_PWD"))
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# paste the URL of the dashboard here
dashboard_url = "https://www.strava.com/dashboard?num_entries=200"
 
driver.get(dashboard_url) # this will open the link

kudos = driver.find_elements(By.XPATH, "//button[@title='Give kudos']")
print("Kudos count is {}".format(len(kudos)))
for k in range(0,len(kudos)):
    if kudos[k].is_displayed():
        athlete = get_athlete_name(kudos[k])
        print(athlete)
        if athlete == 'Nate Treble':
            print('Nate hates bots so no kudos for him')
        else:    
            ActionChains(driver).move_to_element(kudos[k]).click().perform()
        
time.sleep(2)

first_kudos = driver.find_elements(By.XPATH, "//button[@title='Be the first to give kudos!']")
print("First Kudos count is {}".format(len(first_kudos)))
for k in range(0,len(first_kudos)):
    athlete = get_athlete_name(kudos[k])
    print(athlete)
    if athlete == 'Nate Treble':
        print('Nate hates bots so no kudos for him')
    else:    
        try:
            ActionChains(driver).move_to_element(first_kudos[k]).click().perform()
        except:
            break
        
driver.quit()