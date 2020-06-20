"""
@author: hdogrukan
"""
# twitterUserInfo.py Kodu çalıştırdığınız Yere bu python dosyasını oluşturun içine sadece aşağıdaki verileri girin

#          username = "kullanıcı adınız"
#          password = "şifreniz"

from twitterUserInfo import username, password 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions() 
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})#crome ingilizce
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def singIn(self):
        try:
            self.browser.get("https://twitter.com/login") 
            time.sleep(2)
            
           
            usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
            passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
     
           
            usernameInput.send_keys(self.username)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(2)
        except :
            print("Hata1")
               
    def TcloseD(self):
        self.browser.close()

twitter = Twitter(username,password)
twitter.singIn()
time.sleep(10)    
twitter.TcloseD()
            