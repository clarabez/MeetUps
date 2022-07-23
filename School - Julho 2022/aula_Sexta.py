# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {
    "platformName": "Android",
    "appium:deviceName": "Any",
    "appium:appPackage": "com.google.android.calculator",
    "appium:appActivity": "com.android.calculator2.Calculator",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}

# setUp()
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# Elementos numérios
num1 = driver.find_element(by=AppiumBy.ID, value="digit_1")
num2 = driver.find_element(by=AppiumBy.ID, value="digit_2")
num3 = driver.find_element(by=AppiumBy.ID, value="digit_3")
num4 = driver.find_element(by=AppiumBy.ID, value="digit_4")
num5 = driver.find_element(by=AppiumBy.ID, value="digit_5")
num6 = driver.find_element(by=AppiumBy.ID, value="digit_6")
num7 = driver.find_element(by=AppiumBy.ID, value="digit_7")
num8 = driver.find_element(by=AppiumBy.ID, value="digit_8")
num9 = driver.find_element(by=AppiumBy.ID, value="digit_9")
num0 = driver.find_element(by=AppiumBy.ID, value="digit_0")


# Operadores
multiplicar = driver.find_element(by=AppiumBy.ID, value="op_mul")
divisao = driver.find_element(by=AppiumBy.ID, value="op_div")
soma = driver.find_element(by=AppiumBy.ID, value="op_add")
subtracao = driver.find_element(by=AppiumBy.ID, value="op_sub")
igualdade = driver.find_element(by=AppiumBy.ID, value="eq")

# Fluxos
time.sleep(2) # Wait implícito
num1.click()
soma.click()
num5.click()
igualdade.click()
time.sleep(2)
resultado = driver.find_element(by=AppiumBy.ID, value="result_final")
resultado.click()

# TearDown()
driver.quit()