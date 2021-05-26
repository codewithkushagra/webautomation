from selenium import webdriver

url='https://mail.google.com/mail'
driver_location='/home/kushagra/web_automations/utilities/chromedriver'
gmail_username='pythonautomationwithkushagra@gmail.com'
gmail_password='*7417970461#'

driver=webdriver.Chrome(executable_path=driver_location)

driver.get(url)

driver.implicitly_wait(60)
driver.find_element_by_id('identifierId').send_keys(gmail_username)
driver.find_element_by_id('identifierNext').click()

driver.implicitly_wait(60)
driver.find_element_by_name('password').send_keys(gmail_password)
driver.find_element_by_id('passwordNext').click()


