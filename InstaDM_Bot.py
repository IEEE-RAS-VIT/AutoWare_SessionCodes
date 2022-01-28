from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secretKey
import time
my_username=""
my_password=secretKey.password()

usernames=['','','']

messages="Hey!,My new post is up on instagram,Do check it out !"

browser=webdriver.Chrome('chromedriver')

sleep_time=5
def login(username,password):
    browser.get('https://www.instagram.com/')
    time.sleep(sleep_time)
    input_username=browser.find_element_by_name('username')
    input_password=browser.find_element_by_name('password')
    input_username.send_keys(username)
    time.sleep(2)
    input_password.send_keys(password)
    time.sleep(2)
    input_password.submit()
    time.sleep(sleep_time)


def send_messages(users,messages):
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(sleep_time)
    browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    time.sleep(sleep_time)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
    time.sleep(sleep_time)
    for user in users:
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
        time.sleep(sleep_time)
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
        time.sleep(sleep_time)
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div').click()
        time.sleep(sleep_time)
        text_area=browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        text_area.send_keys(messages)
        time.sleep(sleep_time)
        text_area.send_keys(Keys.ENTER)
        print(f'Message successfully sent to {user}')
        time.sleep(sleep_time)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
        time.sleep(sleep_time)






login(my_username,my_password)
time.sleep(sleep_time)
send_messages(usernames,messages)

