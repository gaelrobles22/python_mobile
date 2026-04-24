from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', '.env'))


def get_android_driver():
    print("==> Llamando a get_android_driver con opciones UiAutomator2")
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14.0"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app = "/Users/jonathan.gr/Documents/App versions/Android/Testing/BAC.apk"

    appium_server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")
    return webdriver.Remote(appium_server_url, options=options)
