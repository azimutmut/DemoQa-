from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
def test_get_link():
        browser = webdriver.Chrome()
        browser.get("https://demoqa.com/")
        browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]').click()# go to elements
        time.sleep(2)
        assert browser.current_url == "https://demoqa.com/elements", "Current links is about elements"

        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="item-0"]/span').click()# open text-box

        text_elt = browser.find_element(By.CLASS_NAME, "main-header")#check header
        header_text = text_elt.text
        assert 'Text Box'== header_text, 'its not Text Box'
        time.sleep(2)

        text_elt1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Full Name"]').get_attribute('placeholder')#check placeholder of name
        assert 'Full Name'== text_elt1, 'its not a input of name'
        browser.find_element(By.ID,'userName').send_keys('Name Surname')#input name

        text_elt2=browser.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]').get_attribute('placeholder')#check placeholder of mail
        assert 'name@example.com'== text_elt2, 'its not mail box'
        browser.find_element(By.ID, 'userEmail').send_keys('your@mail.com')#input mail

        text_elt3= browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]').get_attribute('placeholder')#check placeholder of Current Address
        assert 'Current Address'==text_elt3, 'its not a Current Address'
        browser.find_element(By.ID, 'currentAddress').send_keys('Uzbekistan, Tashkent')#input Address

        text_elt4=browser.find_element(By.CSS_SELECTOR, 'label[id="permanentAddress-label"]').text#check valid of this box
        assert 'Permanent Address' == text_elt4, 'its not Permanent Address'
        browser.find_element(By.ID, 'permanentAddress').send_keys('Tashkent, Uzbekistan')#input Permanent Address
        time.sleep(2)

        browser.find_element(By.ID,"submit").click()
        time.sleep(10)
        browser.quit()
