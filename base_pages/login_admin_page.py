class login_admin_page:
  textbox_user_name = "Email"
  textbox_user_password = "Password"
  btn_login_xpath = "//button[@type='submit']"

  def __init__(self, driver):
    self.driver = driver

    def enterUserName():
        self.driver.find_element_by_xpath(self.textbox_user_name).clear()
        self.driver.find_element_by_xpath(self.textbox_user_name).send_keys(self.textbox_user_password)

    def enterPassword():
        self.driver.find_element_by_xpath(self.textbox_user_password).clear

    def login():
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()
