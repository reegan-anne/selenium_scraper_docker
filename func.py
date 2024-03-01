from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
def findAncestors(element: WebElement) -> list[WebElement]:
    # return all ancestors: [parent, ..., <html>]
    return element.find_elements(By.XPATH, ".//ancestor::*")

def findParent(element: WebElement) -> WebElement | None:
    ancestors = findAncestors(element)
    return ancestors[0] if ancestors else None

def findChildren(element: WebElement) -> WebElement | None:
    parent = element
    return parent.find_elements(By.XPATH, '*')

def get_athlete_name(element: WebElement) -> str | None:
    ancestors = findAncestors(element)
    # for a in range(0,len(ancestors)):
    #     # Find top ancestor of that card
    #     if ancestors[a].get_attribute("data-testid")=='web-feed-entry':
    athlete_element = ancestors[12].find_elements(By.XPATH, '//a[@data-testid="owners-name"]')
    return athlete_element