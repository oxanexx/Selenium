from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Учетные данные Github
username = "oxanexx"
password = "password"

# инициализировать драйвер Chrome
driver = webdriver.Chrome(r"chromedriver")

# перейти на страницу входа в github
driver.get("https://github.com/login")

# найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
driver.find_element_by_id("login_field").send_keys(username)

# найти поле ввода пароля и также вставить пароль
driver.find_element_by_id("password").send_keys(password)

# нажмите кнопку входа в систему
driver.find_element_by_name("commit").click()

# ждем завершения состояния готовности
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."

# получаем ошибки (если есть)
errors = driver.find_elements_by_class_name("flash-error")

# при необходимости распечатать ошибки
# для e в ошибках:
#    print(e.text)
# если мы находим это сообщение об ошибке в составе error, значит вход не выполнен
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")