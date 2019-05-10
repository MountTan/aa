from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_ele_times(driver, times, func):  # 等待时间
    return WebDriverWait(driver, times).until(func)


browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.maximize_window()
browser.find_element_by_id('kw').send_keys('python')
ele1 = browser.find_element_by_id('su')
ele1.click()

# xpath1 = browser.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
# xpath1.click()
xpath1 = get_ele_times(browser, 1, lambda browser: browser.find_element_by_xpath('//*[@id="1"]/h3/a[1]'))
xpath1.click()

# browser.quit()
