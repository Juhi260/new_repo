from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Tests.conftest import driver


def wait(func):
    def wrapper(*args,**kwargs):
        obj=args[0]
        locator=args[1]
        webwait=WebDriverWait(obj.driver,10)
        webwait.until(visibility_of_element_located(locator))
        return func(*args,**kwargs)
    return wrapper

class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
    @wait
    def click_item(self, locator):
        self.driver.find_element(*locator).click()
    @wait
    def send_item(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)
    @wait
    def mouse_hover(self,locator):
        act = ActionChains(self.driver)
        ele = self.driver.find_element(*locator)
        act.move_to_element(ele).perform()

    @wait
    def right_click(self,locator):
        act = ActionChains(self.driver)
        ele = self.driver.find_element(*locator)
        act.context_click(ele).perform()

    @wait
    def double_click(self,locator):
        act = ActionChains(self.driver)
        ele = self.driver.find_element(*locator)
        act.double_click(ele).perform()

    @wait
    def scroll_to_element(self,locator):
        act = ActionChains(self.driver)
        ele = self.driver.find_element(*locator)
        act.scroll_to_element(ele).perform()

    @wait
    def scroll_by_amt(self,x,y):
        act = ActionChains(self.driver)
        act.scroll_by_amount(x,y).perform()
    def dropdown_index(self,locator,index):
        sel = Select(self.driver.find_element(*locator))
        sel.select_by_index(index)
    def dropdown_name(self, locator, name):
        sel = Select(self.driver.find_element(*locator))
        sel.select_by_index(name)
    def dropdown_visible_text(self,locator,visible_text):
        sel = Select(self.driver.find_element(*locator))
        sel.select_by_index(visible_text)
    def handle_alert(self,action="accept",value=None):
        try:
            alert = self.driver.switch_to.alert
            if action == "accept":
                alert.accept()
            elif action == "dismiss":
                alert.dismiss()
            elif action == "send_keys" and value:
                alert.send_keys(value)
        except NoAlertPresentException:
            print("No alert present")
    def switch_to_current_window(self,original_window):
        self.driver.switch_to.window(original_window)
    def find_elements(self, locator):
            return self.driver.find_elements(*locator)




