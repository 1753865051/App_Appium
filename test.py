from appium import webdriver

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = 'test'
desired_caps["appPackage"] = 'com.android.settings'
desired_caps['appActivity'] = '.MainSettings'
desired_caps['automationName'] = 'Uiautomator2'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
while True:
    try:
        driver.find_element_by_xpath("//*[@text='小爱同学']").click()
        break
    except Exception:
        driver.swipe(100,1500,100,1000)
