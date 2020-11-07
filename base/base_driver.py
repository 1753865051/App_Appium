from appium import webdriver


def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = 'test'
    desired_caps["appPackage"] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    desired_caps['automationName'] = 'Uiautomator2'
    #是否重置应用
    desired_caps['noReset']=no_reset
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
