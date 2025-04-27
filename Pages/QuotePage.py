from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class QuotePage(BasePage):

    QUOTE_PAGE = (By.XPATH, "//*[@href='quote.html' and @class='nav-item nav-link']")
    REQUEST_BUTTON = (By.XPATH, "//*[@type='submit']")
    NAME_FIELD = (By.ID, "q_name")
    EMAIL_FIELD = (By.ID, "q_email")
    SERVICE_FIELD = (By.ID, "q_service")
    MESSAGE_FIELD = (By.ID, "q_message")
    QUOTE_STATUS_MESSAGE = (By.ID, "quoteStatus")

    def open_quote_page(self):
        self.do_click(self.QUOTE_PAGE)

    def scroll_to_form(self):
        self.do_scroll_to_element(self.REQUEST_BUTTON)

    def fill_in_form(self) -> str:
        self.do_send_keys(self.NAME_FIELD, TestData.username)
        self.do_send_keys(self.EMAIL_FIELD, TestData.user_email)
        self.select_by_index(self.SERVICE_FIELD, 0)
        self.do_send_keys(self.MESSAGE_FIELD, TestData.message)
        self.do_click(self.REQUEST_BUTTON)
        text = self.get_element_text(self.QUOTE_STATUS_MESSAGE)
        return text

    def fill_in_email_field(self, email) -> str:
        self.do_send_keys(self.EMAIL_FIELD, email)
        el = self.get_element(self.EMAIL_FIELD)
        return el.get_attribute('class')



