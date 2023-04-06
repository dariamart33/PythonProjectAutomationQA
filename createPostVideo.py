# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webelement import WebElement


# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
caps = {}
caps["platformName"] = "android"
caps["appium:platformVersion"] = "13"
caps["appium:deviceName"] = "android"
caps["appium:automationName"] = "Appium"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(15)
###
user_action = TouchAction(driver)

###LOOKY####
driver.activate_app("com.looky.app")
time.sleep(3)

##CREATE VIDEO POST###
driver.find_element(By.XPATH,' /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View/android.view.View[3]/android.view.ViewGroup/android.view.ViewGroup').click()
time.sleep(3)
driver.find_element(By.XPATH,' /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup').click()
time.sleep(3)
element_xpath = ' /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]'
element = driver.find_element(By.XPATH, element_xpath)
touch_action = TouchAction(driver)
duration = 1300
touch_action.long_press(element, duration=duration).perform()
time.sleep(65)
###USING Adjust> Brightness###
driver.find_element(By.XPATH,' //android.widget.RelativeLayout[@content-desc="Adjust"]/android.widget.LinearLayout/android.widget.TextView').click()
time.sleep(3)
driver.find_element(By.XPATH,' //android.widget.RelativeLayout[@content-desc="Trim"]/android.widget.LinearLayout/android.widget.ImageView').click()
time.sleep(3)
element_xpath = '//android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.view.View'
element = driver.find_element(By.XPATH, element_xpath)
start_x = element.location['x'] + element.size['width'] // 2
start_y = element.location['y'] + element.size['height'] // 2
end_x = start_x - 300
touch_action.press(x=start_x, y=start_y).wait(100).move_to(x=end_x, y=start_y).release().perform()
time.sleep(3)
driver.find_element(By.ID, ' com.looky.app:id/acceptButton').click()
time.sleep(65)
driver.find_element(By.XPATH,' /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView').click()
time.sleep(65)