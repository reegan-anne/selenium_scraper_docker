from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_athlete_name(kudo_button: WebElement) -> str | None:
    html_str = kudo_button.find_element(By.XPATH, "../../../..").get_attribute('innerHTML')
    soup = BeautifulSoup(html_str, 'lxml')
    links = soup.find_all("a")
    athlete_name = links[1].text.strip()
    return athlete_name