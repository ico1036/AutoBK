from selenium import webdriver
import time


#download_dir = "./"
#options = webdriver.ChromeOptions()

#profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
#        "download.default_directory": download_dir,
#        "download.extensions_to_open": ".pdf"}

#options.add_experimental_option("prefs", profile)

driver = webdriver.Chrome('/home/xoqhdgh/다운로드/chromedriver')#,chrome_options=options)
driver.implicitly_wait(3)
driver.get('http://kudos.knu.ac.kr/pages/index.htm')

driver.maximize_window()

driver.find_element_by_xpath("//a[@title='로그인 바로가기']").click()
driver.find_element_by_id('userid').send_keys('2019226910')
driver.find_element_by_id('passwd').send_keys('941002')
driver.find_element_by_class_name('btn_login').click()
driver.get('http://libproxy.knu.ac.kr/_Lib_Proxy_Url/https://doi.org/10.1016/j.physletb.2020.135425')
driver.find_element_by_id("pdfLink").click()

pdf = driver.find_element_by_xpath("//a[@aria-live='polite']")
file_path = pdf.get_attribute('href')
driver.get(file_path)

time.sleep(3)
driver.close()
