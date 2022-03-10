import sys

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


def init_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.debugger_address = "127.0.0.1:9222"
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--lang=zh-CN")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def judge_xpath_btn(driver, text):
    try:
        target = driver.find_element(By.XPATH, text)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！" + text)
        sys.exit()


def judge_xpath(driver, name):
    try:
        target = driver.find_element(By.XPATH, name)
        return 0
    except NoSuchElementException as ex:
        return 1


def judge_xpath_btn2(driver, text):
    try:
        target = driver.find_element(By.XPATH, "//button[text()='"+ text + "']")
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+text)
        sys.exit()


def judge_xpath_span(driver, text):
    try:
        target = driver.find_element(By.XPATH, "//span[text()='"+ text + "']")
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+text)
        sys.exit()

def judge_class_name(driver, name):
    try:
        target = driver.find_element(By.CLASS_NAME, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()


def judge_class_name_human_valid(driver, name):
    try:
        target = driver.find_element(By.CLASS_NAME, name)
        return 0
    except NoSuchElementException as ex:
        print("人机验证通过，程序继续" + name)
        return 1


def judge_class_name_num(driver, name, num):
    try:
        target = driver.find_elements(By.CLASS_NAME, name)[num]
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()


def judge_id(driver, name):
    try:
        target = driver.find_element(By.ID, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()
