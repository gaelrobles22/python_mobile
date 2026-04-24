from drivers.android_driver import get_android_driver
import time

def test_android_example():
    driver = get_android_driver()
    time.sleep(5)
    assert driver.is_app_installed("com.bac.app")
    driver.quit()
