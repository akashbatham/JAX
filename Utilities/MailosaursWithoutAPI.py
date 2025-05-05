from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Launch browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get("https://mailosaur.com/")
time.sleep(3)
driver.find_element(By.XPATH,'//div[@class="_navAuth_1jcnm_49"]/a[@href="/app"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("akash_batham@softprodigy.com")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("Qwerty123")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
# Step 2: Wait for inbox to load
time.sleep(3)

driver.find_element(By.XPATH,'//div[@class="mt-2"]/a[@href="/app/servers/default/messages/inbox"]').click()
time.sleep(3)
driver.find_element()