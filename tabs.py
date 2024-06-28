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

# To click on the userM tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]').click()
time.sleep(5)

# To click on the job
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
time.sleep(5)

# To click on the organisation
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
time.sleep(5)

# To click on Qualifications
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[4]').click()
time.sleep(5)

# To click on Nationalities
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[5]').click()
time.sleep(5)

# To click on Corporate branding
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[6]').click()
time.sleep(5)

# To click on config tab
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[7]').click()
time.sleep(5)

# To click on PIM
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)

# To click on under_config
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]').click()
time.sleep(5)

# To click on employee_list
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
time.sleep(5)

# To click on under_add_employee
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
time.sleep(5)

# To click on under_add_reports
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[4]').click()
time.sleep(5)
