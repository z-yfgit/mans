from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "www.example.com"
driver.get(url)
select_element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'www')]"))
            
        )

"""
EC.element_to_be_clickable((By.ID, "element_id"))
EC.element_to_be_clickable((By.NAME, "element_name"))
EC.element_to_be_clickable((By.CLASS_NAME, "btn-login"))
"""

### 元素操作

# 点击元素
select_element.click()

# 输入文本
select_element.send_keys("输入的文本")

# 获取元素属性
select_element.get_attribute("class")