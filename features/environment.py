from utils.browser_factory import get_browser
import os


def before_all(context):
    context.driver = get_browser("chrome")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://demowebshop.tricentis.com")

def before_scenario(context, scenario):
    print("Starting scenario: " + scenario.name)


def after_scenario(context, scenario):
    if scenario.status in ["failed", "error","passed"]:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        file_name = scenario.name.replace(" ", "_")
        context.driver.save_screenshot(
            f"screenshots/{file_name}_{scenario.status}.png"
        )

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()
