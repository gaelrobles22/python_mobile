import os
from dotenv import load_dotenv
from drivers.android_driver import get_android_driver

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', '.env'))


def before_scenario(context, scenario):
    print(f"\n➡️ Iniciando escenario: {scenario.name}")

    # Puedes leer variables de entorno para configurar driver
    context.appium_server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723/wd/hub")

    # Aquí puedes modificar get_android_driver para aceptar URL si quieres,
    # o directamente crear driver aquí con desired_caps cargadas de env si prefieres.
    context.driver = get_android_driver()  # Si quieres, adapta get_android_driver para usar context.appium_server


def after_scenario(context, scenario):
    print(f" Escenario terminado: {scenario.name}")
    if hasattr(context, "driver"):
        context.driver.quit()