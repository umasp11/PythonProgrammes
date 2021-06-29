from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert

driver=webdriver.Chrome (r"C:\Users\umasankar.panigrahy\Downloads\chromedriver_win32\chromedriver.exe")
action= ActionChains(driver)
driver.maximize_window()
#driver.get('https://www.myntra.com/')
#menu= driver.find_element_by_xpath("//a[@data-group='men']")

#action.move_to_element(menu).perform()
#driver.find_element_by_xpath("//a[text()='Sweatshirts']").click()

driver.get('https://www.myntra.com/')

men=driver.find_element_by_xpath("//a[@href='/shop/men' and @class='desktop-main']")
Tshirts= driver.find_element_by_xpath("//a[@href='/men-tshirts']")
action.move_to_element(men).move_to_element(Tshirts).click().perform()