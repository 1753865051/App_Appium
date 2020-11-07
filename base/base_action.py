from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self,message):
        message_xpath=By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.find_element(message_xpath)
            return True
        except Exception:
            return False
    def get_toast_text(self,message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath).text
        else:
            raise Exception("toast-Exception!!!")

    def scroll_page_one_time(self,direction="up"):
        """
        :param direction:
        :return:
        """
        width = self.driver.get_window_size()["width"]
        heigth = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = width / 2
        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = heigth / 4 * 1
        bottom_x = center_x
        bottom_y = heigth / 4 * 3
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def find_element_with_scroll(self,feature,direction="up"):

        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)
                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source
