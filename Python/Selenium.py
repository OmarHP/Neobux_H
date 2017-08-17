import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")

driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.neobux.com')
loginLink = driver.find_element_by_link_text('Iniciar Sesión')
loginLink.click()

usernameInput = driver.find_element_by_id('Kf1')
password1Input = driver.find_element_by_id('Kf2')
password2Input = driver.find_element_by_id('Kf4')

usernameInput.send_keys('OmarHP90m')
password1Input.send_keys('@59754851hp')
password2Input.send_keys('@59754851hp')

time.sleep(20) # Let the user actually see something!
submitButton = driver.find_element_by_id('botao_login')
submitButton.click()


anunciosLink = driver.find_element_by_link_text('Ver Anuncios')
anunciosLink.click()

n = len(driver.find_elements_by_class_name('mbxm'))
print(n)
main_window = driver.current_window_handle

for i in range(1,n+1):
    try:
        flag = driver.find_element_by_css_selector('#da'+str(i)+'a .adfu')
        advertising = driver.find_element_by_id('da'+str(i)+'a')
        advertising.click()
        time.sleep(2) # Let the user actually see something!
        driver.find_element_by_css_selector('#da'+str(i)+'c a').click()
        time.sleep(30) # Let the user actually see something!
        driver.switch_to_window(main_window)

    except NoSuchElementException:
        continue
        













driver.quit()
