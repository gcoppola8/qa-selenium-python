import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import solution


class BBCWeatherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        try:
            cls.driver.quit()
        except:
            pass

    def test_get_weather_minus_1(self):
        self.assertEqual(None, solution.get_weather(self.driver, -1))

    def test_get_weather_0(self):
        self.assertEqual(None, solution.get_weather(self.driver, 0))

    def test_get_weather_11(self):
        self.assertEqual(None, solution.get_weather(self.driver, 11))

    def test_get_weather_5_for_sofia(self):
        self.driver.get('http://www.bbc.com/weather/727011')
        result = solution.get_weather(self.driver, 5)

        day_values = self.driver.find_elements(By.CLASS_NAME, 'wr-day__content')
        self.assertEqual(len(result), 5)
        

    def test_get_weather_10_for_new_york(self):
        self.driver.get('http://www.bbc.com/weather/5128581')
        result = solution.get_weather(self.driver, 10)

        day_values = self.driver.find_elements(By.CLASS_NAME, 'wr-day__content')
        self.assertEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()
