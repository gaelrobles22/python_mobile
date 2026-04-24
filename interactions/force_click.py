from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def force_click_by_coordinates(driver, element, offset_x=10, offset_y=10):
    loc = element.location
    size = element.size

    x = loc['x'] + offset_x
    y = loc['y'] + offset_y

    print(f"[force_click] Tap en coordenadas: ({x}, {y})")

    pointer = PointerInput(PointerInput.TOUCH, "finger1")
    actions = ActionBuilder(driver)
    actions.add_action(pointer.create_pointer_move(duration=0, x=x, y=y))
    actions.add_action(pointer.create_pointer_down())
    actions.add_action(pointer.create_pointer_up())
    actions.perform()


def send_input(context, locator, value, timeout=5, force_click=False, clear_first=True):
    # Espera y obtiene el elemento antes del click
    element = WebDriverWait(context.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    print(f"Elemento visible: {element.is_displayed()}, habilitado: {element.is_enabled()}")

    if force_click:
        force_click_by_coordinates(context.driver, element)
    else:
        element.click()

    if clear_first:
        # Vuelve a obtener el elemento para clear
        element = WebDriverWait(context.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.clear()
        except Exception as e:
            print(f"Advertencia clear(): {e}")

    # Vuelve a obtener el elemento para send_keys
    element = WebDriverWait(context.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.send_keys(value)

    try:
        context.driver.hide_keyboard()
    except Exception:
        pass