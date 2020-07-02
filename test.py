from selenium import webdriver
import unittest
import time
class Test_login(unittest.TestCase):
    def setUp(self):
        self.h=webdriver.Chrome()
    def test(self):
        self.h.get('http://192.168.0.119:5025/login')
        time.sleep(1)
    def test222(self):
        self.h.get('http://192.168.0.119:5025/login')
        self.h.find_element_by_id('text').send_keys('sun')
        self.h.find_element_by_id('password').send_keys('zhen')
        self.h.find_element_by_id('zzzzzz').click()
    def tearDown(self):
        self.h.quit()
if __name__ =='__main__':
    unittest.main()