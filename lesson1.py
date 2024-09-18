import time
from playwright.sync_api import sync_playwright

# # playwright also supports async

# URL = 'https://minneapolis.craigslist.org/'

# # This is to launch a playwright session
# playwright = sync_playwright().start()

# # Playwright supports multiple browsers
# # firefox, chrmium, and webkit

# # browser = playwright.webkit.launch(headless=False)
# # browser = playwright.firefox.launch(headless=False)
# browser = playwright.chromium.launch(headless=False)

# # page is the same thing as a tab
# # Viewport is for browser size when running
# page = browser.new_page(
#     java_script_enabled=True,
#     viewport={'width': 200, 'height': 100}
#     # viewport={'width': 1920, 'height': 1080}
# )
# # wait_until: When to consider operation succeeded, defualts to load.
# page.goto(URL, wait_until='load')

# time.sleep(10)

# page.close()
# browser.close()
# playwright.stop()


# Cleaned up code version
def run_playwright(url):
    with sync_playwright() as playwright:
        with playwright.chromium.launch(headless=False) as browser:
            page = browser.new_page(
                java_script_enabled=True,
                viewport={'width': 1920, 'height': 1080}
            )
            page.goto(url, wait_until='load')
            time.sleep(5)
            page.close()


def main():
    URL = 'https://minneapolis.craigslist.org/'
    run_playwright(URL)

main()