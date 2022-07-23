from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


desired_cap = {
    'platformName': 'Android',
    "deviceName": "emulator-5554",
    'autoGrantPermissions': True,
    'newCommandTimeout': 300,
    'appPackage': 'com.google.android.calculator',
    'appActivity': 'com.android.calculator2.Calculator'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

num0 = "digit_0"
num1 = "digit_1"
num2 = "digit_2"
num3 = "digit_3"
num4 = "digit_4"
num5 = "digit_5"
num6 = "digit_6"
num7 = "digit_7"
num8 = "digit_8"
num9 = "digit_9"

result = "result"
sum = "op_add"
equals = "eq"
result = "result_final"

def test_one():
    time.sleep(1)
    driver.find_element(by=AppiumBy.ID, value=num1).click()
    driver.find_element(by=AppiumBy.ID, value=sum).click()
    driver.find_element(by=AppiumBy.ID, value=num5).click()
    driver.find_element(by=AppiumBy.ID, value=equals).click()

    time.sleep(3)
    resultado = driver.find_element(by=AppiumBy.ID, value=result).text
    assert resultado=='6', resultado

test_one()
