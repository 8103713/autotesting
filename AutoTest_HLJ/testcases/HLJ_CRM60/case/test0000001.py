from selenium import webdriver
import time
option = webdriver.ChromeOptions()
option.add_argument('--disable-popup-blocking')
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6&rsv_spt=1&rsv_iqid=0xd43bba540002ba3f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=5&rsv_sug1=1&rsv_sug7=001")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")