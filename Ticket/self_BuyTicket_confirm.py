#使用ChroPath找路徑
import keyboard
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class webtest_php(unittest.TestCase):  # 測試項目
    def setUp(self):
        self.verificationErrors=[]
        service = Service(executable_path=r"C:\Users\Cheng\Downloads\工具安裝包\edgedriver_win64\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service) #使用edge瀏覽器
        # 要執行自動測試的網站
        self.url_1 = "https://kktix.com/users/sign_in?back_to=https%3A%2F%2Fkktix.com%2F" # KKTIX登入頁面
        self.url_2 = "address" # 想要購票的網站

    def test_login(self):
        driver = self.driver
        driver.get(self.url_1) # 跳轉網頁
        #driver.maximize_window() # 網頁全螢幕
        user=driver.find_element(By.NAME, "user[login]") # 找到使用者名稱框
        user.send_keys('name') # 使用者名稱
        passwd=driver.find_element(By.NAME, "user[password]") # 找到使用者密碼框
        passwd.send_keys('code' + Keys.ENTER) # 使用者密碼
        driver.get(self.url_2) # 跳轉網頁
        input_elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/div[5]/div[2]/div[4]/div[1]/div/div/span[4]/input") # 使用 XPath 定位
        input_elem.clear() # 清除<input> 內容
        input_elem.send_keys("1") # 填入<input> 新內容
        chkbox = driver.find_element(By.ID, "person_agree_terms") # 定位到該 checkbox ID
        if not chkbox.is_selected(): #如果 checkbox 未勾選,使用 click() 方法勾選它
            chkbox.click()

        for i in range(3): # 確認按鈕
            keyboard.press_and_release("tab") # 鍵盤輸入tab

        keyboard.press_and_release("enter") # 鍵盤輸入enter
        sleep(99999)

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
#無法確認上傳
