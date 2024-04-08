from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
#browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
wait = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button1 = browser.find_element(By.TAG_NAME, "button")
button1.click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
print (y)
input1 = browser.find_element(By.CLASS_NAME, "form-control")
input1.send_keys(y)
button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
button2.click() 


