import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.common.exceptions import NoSuchElementException

def buy_item(item_name):

    sauce = False
    if sauce:
        caps = {}
        caps = {}
        caps['platformName'] = 'Android'
        caps['appium:app'] = 'storage:filename=mda-1.0.17-20.apk' # The filename of the mobile app
        #caps['appium:deviceName'] = 'Samsung Galaxy S6 GoogleAPI Emulator'
        #caps['appium:platformVersion'] = '8.0'
        caps['appium:deviceName'] = 'Android GoogleAPI Emulator'
        caps['appium:platformVersion'] = '6.0'
        caps['appium:automationName'] = 'UiAutomator2'
        caps['sauce:options'] = {}
        caps['sauce:options']['appiumVersion'] = '1.22.3'
        caps['sauce:options']['build'] = '0.1.1'
        caps['sauce:options']['name'] = "Test2BuyStuff"
        caps["appium:autoGrantPermissions"] = True
        caps["appium:appWaitActivity"] = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
        #caps["app"] = "https://github.com/saucelabs/my-demo-app-android/releases/download/1.0.17/mda-1.0.17-20.apk"
        #caps["appium:app"] = "C:\\Users\\kenton\\Downloads\\mda-1.0.17-20.apk"
        #caps["broswerVersion"] = "latest"

        url = "https://oauth-kentonself-8f06d:bf62e5a3-2d95-4323-830c-a9b7d658010f@ondemand.us-west-1.saucelabs.com:443/wd/hub"
        driver = webdriver.Remote(url, caps)
    else:
        caps = {}
        caps["browserName"] = "firefox"
        caps["platformName"] = "Android"
        caps["appium:platformVersion"] = "11.0"
        caps["appium:deviceName"] = "Android Emulator"
        caps["appium:app"] = "C:\\Users\\kenton\\Downloads\\mda-1.0.17-20.apk"
        caps["appium:autoGrantPermissions"] = True
        caps["appium:appWaitActivity"] = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        driver = webdriver.Remote("http://192.168.68.53:4723/wd/hub", caps)
        #driver = webdriver.Remote("http://ks_hp_laptop.local:4723/wd/hub", caps)

    driver.implicitly_wait(time_to_wait=10)

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=item_name)
    el1.click()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(368, 832)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(354, 196)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el2 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/start3IV")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Closes review dialog")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Gray color")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Increase item quantity")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Increase item quantity")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Decrease item quantity")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
    el8.click()
    el9 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cartIV")
    el9.click()
    el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Confirms products for checkout")
    el10.click()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(265, 777)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(312, 331)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el11 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/username1TV")
    el11.click()
    el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to login with given credentials")
    el12.click()
    el13 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/fullNameET")
    el13.click()
    el13.send_keys("Kenton Self")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(400, 522)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(385, 208)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el14 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address2ET")
    el14.click()
    el14.send_keys("Suite 123")
    el15 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address1ET")
    el15.click()
    el15.send_keys("1210 Clarice")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(303, 497)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(305, 82)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el16 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cityET")
    el16.click()
    el16.send_keys("Dallas")
    el17 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/stateET")
    el17.click()
    el17.send_keys("Texas")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(326, 539)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(347, 143)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(166, 1225)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el18 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/zipET")
    el18.click()
    el18.send_keys("75248")
    el19 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/countryET")
    el19.click()
    el19.send_keys("USA")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(185, 1219)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el20 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saves user info for checkout")
    el20.click()
    el21 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
    el21.click()
    el21.send_keys("Kenton Self")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(352, 486)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(358, 101)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el22 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cardNumberET")
    el22.click()
    el22.send_keys("4444444444444448")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(179, 1215)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el23 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/expirationDateET")
    el23.click()
    el23.send_keys("03/24")
    el24 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/securityCodeET")
    el24.click()
    el24.send_keys("123")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(179, 1211)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el25 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saves payment info and launches screen to review checkout data")
    el25.click()
    el26 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Completes the process of checkout")
    el26.click()

    try:
        driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/completeTV")
    except NoSuchElementException:
        pytest.fail("Order did not complete")

    driver.quit()


def test_buy_back_pack():
    buy_item("Sauce Lab Back Packs")


def test_buy_bike_light():
    buy_item("Sauce Lab Bike Light")
