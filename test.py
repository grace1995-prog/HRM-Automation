from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(30)
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(5)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(5)

# To click on the admin tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(5)

# To click on PIM
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)

# To click on Leave tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
time.sleep(5)

# To click on next Tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
time.sleep(5)

# To click on temps tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()
time.sleep(5)

# To click on recruitment tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()
time.sleep(5)

# To click on Mes info tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
time.sleep(5)

# To click on Performance tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a').click()
time.sleep(5)

# To click on Table de bord tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').click()
time.sleep(5)

# To click on directory tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()
time.sleep(5)

# To click on maintenance tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()
time.sleep(5)

# To click on the cancel button
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/form/div[4]/button[1]').click()
time.sleep(5)

time.sleep(5)
# To click on claim tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').click()
time.sleep(5)

# To click on Buzz tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a').click()
time.sleep(5)

# Close the browser
driver.quit()
