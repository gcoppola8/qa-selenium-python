from selenium import webdriver
from selenium.webdriver.common.by import By


def get_weather(driver: webdriver, days: int):
    if days is None or days < 1 or days > 10:
        return None
    result = []
    days_div = driver.find_elements(By.CLASS_NAME, 'wr-day__content')
    for i in range(days+1):
        wr_type = days_div[i].find_element(By.CLASS_NAME, 'wr-weather-type__text').text
        h_temp = days_div[i].find_element(By.CLASS_NAME, 'wr-value--temperature--c').text
        result.append((wr_type, h_temp))

    return result
