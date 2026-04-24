from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.LoginView import LoginView
from interactions.force_click import force_click_by_coordinates
from interactions.force_click import send_input

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', '.env'))


@given("El usuario está en la vista de Login")
def step_impl(context):
    pass

@then("el usuario ingresa los datos de autenticación e inicia la sesión")
def step_impl(context):

    username_field = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(LoginView.USERNAME_FIELD)
    )
    username_field.click()
    context.driver.hide_keyboard()
    username_field.send_keys("cesar.tae")
    context.driver.hide_keyboard()

    password_field = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(LoginView.PASSWORD_FIELD)
    )
    # context.driver.hide_keyboard()
    password_field.click()
    context.driver.hide_keyboard()
    password_field.send_keys("Passw.018")
    context.driver.hide_keyboard()


    login_button = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(LoginView.LOGIN_BUTTON)
    )
    login_button.click()


# @then("el usuario ingresa los datos de autenticación e inicia la sesión")
# def step_impl(context):
#     # Usamos click normal para username
#     send_input(context, LoginView.USERNAME_FIELD, "cesar.tae", force_click=False)
#     # Usamos click forzado para password
#     send_input(context, LoginView.PASSWORD_FIELD, "Passw.018", force_click=True)
#
#     login_button = WebDriverWait(context.driver, 5).until(
#         EC.element_to_be_clickable(LoginView.LOGIN_BUTTON)
#     )
#     login_button.click()