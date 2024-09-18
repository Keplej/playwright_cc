import time
from playwright.sync_api import sync_playwright

# Here we are demostrating multiple brower instances
# Each browser has its own cookies, browser, and session data

URL = 'https://minneapolis.craigslist.org/'

# This is to launch a playwright session
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)

# Browser instance #1
browser_context1 = browser.new_context(java_script_enabled=True)
browser_context1_page = browser_context1.new_page()
browser_context1_page.goto(URL, wait_until='load')

time.sleep(2)

# Browser instance #2
browser_context2 = browser.new_context(java_script_enabled=True)
browser_context2_page = browser_context2.new_page()
browser_context2_page.goto(URL, wait_until='load')

time.sleep(2)

# Clean up
print("Cleaning up...")
browser_context1_page.close()
browser_context2_page.close()
browser_context1.close()
browser_context2.close()
browser.close()
playwright.stop()