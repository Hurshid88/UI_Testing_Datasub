from Config.config import TestData
from Pages.QuotePage import QuotePage
from Tests.test_base import BaseTest


class TestQuotePage(BaseTest):
    quote_page = None

    def test_quote_form(self):
        self.boilerplate()
        text = self.quote_page.fill_in_form()
        assert "success" in text or "успешно" in text, "Success message is not visible. Test failed"
        print("Success message is visible. Test passed")

    def test_quote_form_with_invalid_email(self):
        self.boilerplate()
        attribute = self.quote_page.fill_in_email_field(TestData.invalid_email)
        assert "invalid" in attribute, "Form is accepting invalid email. Test failed"
        print("Form isn't accepting invalid_email. Test passed")

    def boilerplate(self):
        if self.quote_page:
            pass
        else:
            self.quote_page = QuotePage(self.driver)
        self.quote_page.open_quote_page()
        self.quote_page.scroll_to_form()

