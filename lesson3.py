import time
from playwright.sync_api import sync_playwright

# Taking a screenshot in playwright

URL = 'https://minneapolis.craigslist.org/hnp/apa/d/minneapolis-in-minneapolis-community/7785349988.html'

# This is to launch a playwright session
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page(java_script_enabled=True)
page.goto(URL, wait_until='load')

time.sleep(2)

file_name = 'screenshot.jpeg'

page.screenshot(
    path=file_name,
    full_page=True, # This will screen shot the entire page, if False it will only screen shot the visiable area
    omit_background=True, # only works with png
    type='jpeg',
    quality=100 # available only when type='jpeg'
)

page.close()
browser.close()
playwright.stop()
