import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup


def get_peaktiming_stats(url):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize the browser driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Access the url
    driver.get(url)
    driver.maximize_window()
    # Create action chain object
    action = ActionChains(driver)

    # Go to full results tab after a little wait for loading
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@id='menu_results']").click()

    time.sleep(2)
    total = driver.find_element(By.XPATH, "//*[@id='divResults_Status']").get_attribute("innerHTML")
    print(total)

    driver.find_element(By.XPATH, "//*[@id='list_results']/table/tbody/tr[1]").click()
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

    # Get fully loaded htmldata into dataframe
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    div=soup.select_one("div#list_results")
    table=pd.read_html(str(div))
    df = table[0]

    # Format the df
    df.columns = df.iloc[0]
    df = df[1:]
    print(df.head())

    driver.quit()
    
    return df