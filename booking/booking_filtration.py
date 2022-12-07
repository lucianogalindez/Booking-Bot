# This file will include a class with instance methods
# That will be responsible to intereact with our website
# After we have some results, to apply filtrations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:

    def __init__(self, driver:WebDriver):

        self.driver = driver

    def apply_star_rating(self, *star_values):

       star_filtrarion_box = self.driver.find_element(
        By.CSS_SELECTOR,
        "div[data-filters-group = 'class']"
       )

       star_child_element = star_filtrarion_box.find_elements(
        By.CSS_SELECTOR,
        '*'
       )

       for star_value in star_values:
            for star_element in star_child_element:
                if (str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars') | (str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} star'):
                    star_element.click()
 
       print(len(star_child_element))

