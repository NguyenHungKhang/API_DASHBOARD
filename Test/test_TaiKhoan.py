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
from selenium.webdriver.chrome.options import Options
import connection

ENDPOINT = "http://ec2-3-82-188-235.compute-1.amazonaws.com:8080/"

  
def test_tCTaiKhoan001():
  driver = connection.test_connection_driver()
  driver.maximize_window()
  wait = WebDriverWait(driver, timeout=10)

  driver.get(ENDPOINT)
  driver.set_window_size(974, 1032)
  driver.find_element(By.LINK_TEXT, "Login").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
  driver.find_element(By.CSS_SELECTOR, "button").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
  driver.find_element(By.CSS_SELECTOR, "input").click()

  driver.quit()
  
def test_tCTaiKhoan002():
  driver = connection.test_connection_driver()
  driver.maximize_window()
  wait = WebDriverWait(driver, timeout=10)

  driver.get(ENDPOINT)
  driver.set_window_size(974, 1032)
  driver.find_element(By.LINK_TEXT, "Login").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
  driver.find_element(By.CSS_SELECTOR, "button").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
  driver.find_element(By.CSS_SELECTOR, "input").click()
  driver.find_element(By.CSS_SELECTOR, "th > button").click()
  element = driver.find_element(By.CSS_SELECTOR, "th > button")
  actions = ActionChains(driver)
  actions.move_to_element(element).perform()
  element = driver.find_element(By.CSS_SELECTOR, "body")
  actions = ActionChains(driver)
  actions.move_to_element(element, 0, 0).perform()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("nguyenhungkhang321@gmail.com")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").send_keys("123")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(6)").send_keys("1")
  driver.find_element(By.CSS_SELECTOR, ".modal-body").click()
  driver.find_element(By.CSS_SELECTOR, ".modal-right-button").click()
  driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
  driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3) > p").click()

  driver.quit()
  
def test_tCTaiKhoan003():
  driver = connection.test_connection_driver()
  driver.maximize_window()
  wait = WebDriverWait(driver, timeout=10)

  driver.get(ENDPOINT)
  driver.set_window_size(974, 1032)
  driver.find_element(By.LINK_TEXT, "Login").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
  driver.find_element(By.CSS_SELECTOR, "button").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
  driver.find_element(By.CSS_SELECTOR, "input").click()
  driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
  driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2) > p").click()
  driver.find_element(By.ID, "inputStatus").click()
  driver.find_element(By.ID, "inputStatus").send_keys("0")
  driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()

  driver.quit()
  
def test_tCTaiKhoan004():
  driver = connection.test_connection_driver()
  driver.maximize_window()
  wait = WebDriverWait(driver, timeout=10)

  driver.get(ENDPOINT)
  driver.set_window_size(974, 1032)
  driver.find_element(By.LINK_TEXT, "Login").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
  driver.find_element(By.CSS_SELECTOR, "button").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
  driver.find_element(By.CSS_SELECTOR, "input").click()
  driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right").click()
  driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) .svg-inline--fa").click()

  driver.quit()
  
def test_tCTaiKhoan005():

  driver = connection.test_connection_driver()
  driver.maximize_window()
  wait = WebDriverWait(driver, timeout=10)

  driver.get(ENDPOINT)
  driver.set_window_size(974, 1032)
  driver.find_element(By.LINK_TEXT, "Login").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("admin@admin.com")
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
  driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("1")
  driver.find_element(By.CSS_SELECTOR, "button").click()
  driver.implicitly_wait(3)
  driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) img").click()
  driver.find_element(By.CSS_SELECTOR, "input").click()
  driver.find_element(By.CSS_SELECTOR, "input").send_keys("ngh")
  driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").click()

  driver.quit()
