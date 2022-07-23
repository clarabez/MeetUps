from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    'platformName': 'Android',
    "deviceName": "emulator-5554",
    'autoGrantPermissions': True,
    'newCommandTimeout': 300,
    'app': '/home/mabezerr/Documents/pessoal/aulas/appium-java/src/test/java/resources/app-curso.apk',
    'appPackage': 'com.example.cursoappium',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

btnCadastrarPessoa = "button_cadastrar"
textInputNome = "TextInputNome"
textInputEmail = "TextInputEmail"
btnCadastrar = "BotaoCadastrar"

cadastrar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, btnCadastrarPessoa)))
cadastrar.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, textInputNome)))
driver.find_element(by=AppiumBy.ID, value=textInputNome).send_keys("Maria4")
driver.find_element(by=AppiumBy.ID, value=textInputEmail).send_keys("Maria@test.com")
driver.find_element(by=AppiumBy.ID, value=btnCadastrar).click()

#assert driver.find_element(by=AppiumBy.PARTIAL_LINK_TEXT, "Cadastro realizado com sucesso").text
#assert driver.find_element(By.XPATH("//contains[text(),“Cadastro realizado com sucesso”"))
#assert WebDriverWait(driver, 10).until(EC.xpath(("Cadastro realizado com sucesso")))