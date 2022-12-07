from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime as dt

class Booking(webdriver.Chrome) :

    def __init__(self, teardown=False, options=Options):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tab):
        if self.teardown:
            self.quit()

    def land_first_page(self, constant):
        self.get(constant.BASE_URL)
        #input()

    def change_currency(self, currency):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 
            "button[data-tooltip-text = 'Choose your currency']"
        )
        currency_element.click()

        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            f"a[data-modal-header-async-url-param *= 'selected_currency={currency}']"
        )
        selected_currency_element.click()
        #input()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.ID, 
            'ss'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR,
            "li[data-i = '0']"
        )
        first_result.click()
        #input()

    def select_dates (self, check_in_date, check_out_date):

        today = dt.date.today()
        d_checkin = dt.datetime.strptime(check_in_date, '%Y-%m-%d')
        d_checkout = dt.datetime.strptime(check_out_date, '%Y-%m-%d')

        diff_today_checkin = (d_checkin.year - today.year) * 12 + d_checkin.month - today.month

        calendar_next = self.find_element(
            By.CSS_SELECTOR,
            "div[data-bui-ref = 'calendar-next']"
        )

        # This logic will allow to move automatically the calendar when the user selects a future date
        if (diff_today_checkin > 1) :
            i = diff_today_checkin
            while (i > 1):
                calendar_next.click()
                i = i - 1

        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f"td[data-date = '{check_in_date}']"
        )
        check_in_element.click()

        diff_checkin_checkout = (d_checkout.year - d_checkin.year) * 12 + d_checkout.month - d_checkin.month

        if (diff_checkin_checkout > 0) :
            i = diff_checkin_checkout
            while (i > 0):
                calendar_next.click()
                i = i - 1

        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f"td[data-date = '{check_out_date}']"
        )
        check_out_element.click()

        #input('hola')

    def select_adults(self, adults):
        
        selection_element = self.find_element(
            By.ID,
            "xp__guests__toggle"
        )
        selection_element.click()

        add_button = self.find_element(
            By.CSS_SELECTOR,
            "button[data-bui-ref = 'input-stepper-add-button']"
        )

        subs_button = self.find_element(
            By.CSS_SELECTOR,
            "button[data-bui-ref = 'input-stepper-subtract-button']"
        )

        if (adults > 2):
            i = adults - 2
            while (i > 0):
                add_button.click()
                i = i - 1
        elif (adults < 2): # this option is just for those cases when I look for 1 person
            subs_button.click()

    def complete_search(self):

        search_button = self.find_element(
            By.CSS_SELECTOR,
            "button[data-sb-id = 'main']"
        )
        search_button.click()

    def apply_filtrations(self, newclass):
        
        filtration = newclass(driver = self)

        filtration.apply_star_rating(2,3,1)

        input()
