from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

from selenium import webdriver


driver = webdriver.Chrome(options=option,executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=ca")
driver.maximize_window()

driver.find_element_by_id("username").send_keys("pramod.nice@gmail.com")
driver.find_element_by_id("password").send_keys("986Auto@z")
driver.find_element_by_name("Login").click()
driver.implicitly_wait(5)
