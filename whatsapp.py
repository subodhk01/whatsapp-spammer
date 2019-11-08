from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('http://web.whatsapp.com')

subodhk=input('Press any key after scanning QR ')

while True:
    passk=(input("Enter Password: "))
    if(passk=='admin'):
        name = input('Name of the user or the group : ')
        msg = input('Enter the msg to spam: ')
        count = int(input('Number of times you want to send the message : '))
        
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        time.sleep(2)
        element = driver.find_element_by_class_name("_3u328")
        for i in range(1, count+1):
            try:
                element.send_keys(msg)
                element.send_keys(Keys.ENTER)
                print(i)
                time.sleep(0.3)
                if i % 100 == 0:
                    time.sleep(15)
            except:
                print(i,"error in loop")
                time.sleep(0.75)        
    subodhk=input("Do you wish to exit (y/n) : ")
    if subodhk == "y":
        break
    else:
        pass

subodhk=input("Have fun, enjoy!! \n Peace - subodhk \n http://github.com/subodhk01/whatsapp-spammer \n")
