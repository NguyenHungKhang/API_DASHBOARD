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

ENDPOINT = "http://ec2-54-90-106-213.compute-1.amazonaws.com:8080/"

class TestTCDangNhap001():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCDangNhap001(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("nguyenhungkhang100@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(10.0)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()

class TestTCDangNhap002():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCDangNhap002(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("nguyenhungkhang123@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("321")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(10.0)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()

class TestTCDangNhap003():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCDangNhap003(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("nguyenhungkhang123@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(30)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) img").click()

class TestTCDangNhap004():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCDangNhap004(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(10.0)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()

class TestTCDangNhap005():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, timeout=10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCDangNhap005(self):
    self.driver.get(ENDPOINT)
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.implicitly_wait(30)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) img").click()