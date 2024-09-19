""" File Download """
import time
from playwright.sync_api import sync_playwright


URL = 'https://the-internet.herokuapp.com/download'
xpath_prefix = 'xpath='

# This is to launch a playwright session
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page(java_script_enabled=True)
page.goto(URL, wait_until='load')

image_xpath_query ='//a[@href="download/webdriverIO.png"]'
page.wait_for_selector(xpath_prefix + image_xpath_query, timeout=5000)

# Initiate file download
with page.expect_download() as download_info:
    page.get_by_text('webdriverIO.png').click()

# Wait for the download to complete
download = download_info.value

suggested_filename = download.suggested_filename
print(f'Download started: {suggested_filename}')

# Save the file
download.save_as(suggested_filename)

page.close()
browser.close()
playwright.stop()
