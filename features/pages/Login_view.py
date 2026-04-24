from appium.webdriver.common.appiumby import AppiumBy

class LoginView:
    USERNAME_FIELD = (AppiumBy.XPATH, '//android.view.View[@content-desc="Usuario"]/android.widget.EditText')
    PASSWORD_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)')
    LOGIN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Ingresar")')