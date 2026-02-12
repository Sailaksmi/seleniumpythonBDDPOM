# from utils.browser_factory import get_browser
import os

from utils.browser_factory import get_browser


def before_scenario(context, scenario):
    print("Starting scenario: " + scenario.name)

    context.driver = get_browser("chrome")
    context.driver.maximize_window()
    context.driver.get("https://demowebshop.tricentis.com")


def after_scenario(context, scenario):

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    file_name = scenario.name.replace(" ", "_")
    screenshot_path = f"screenshots/{file_name}_{scenario.status}.png"

    context.driver.save_screenshot(screenshot_path)
    context.driver.quit()
