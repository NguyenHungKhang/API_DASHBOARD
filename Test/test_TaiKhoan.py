# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')
# optional
chrome_options.add_argument('--no-sandbox')
# optional
chrome_options.add_argument('--disable-dev-shm-usage')
webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

ENDPOINT = "http://ec2-54-90-106-213.compute-1.amazonaws.com:8080/"

class TestTCTaiKhoan001():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCTaiKhoan001(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()

class TestTCTaiKhoan002():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCTaiKhoan002(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, "th > button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "th > button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("nguyenhungkhang321@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(6)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, ".modal-body").click()
    self.driver.find_element(By.CSS_SELECTOR, ".modal-right-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3) > p").click()

class TestTCTaiKhoan003():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCTaiKhoan003(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2) > p").click()
    self.driver.find_element(By.ID, "inputStatus").click()
    self.driver.find_element(By.ID, "inputStatus").send_keys("0")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()

class TestTCTaiKhoan004():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCTaiKhoan004(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) .svg-inline--fa").click()

class TestTCTaiKhoan005():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCTaiKhoan005(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("ngh")
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").click()