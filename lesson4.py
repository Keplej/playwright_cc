""" Mouse Interactions """
import time
from playwright.sync_api import sync_playwright

# What we are doing in this lesson is to simulate mouse clicking on the mouse click test

URL = 'https://clickspeedtest.com/'

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)

page = browser.new_page(java_script_enabled=True)
page.goto(URL, wait_until='load')

xpath_query = '//button[@id="clicker"]'
button_element = page.wait_for_selector(xpath_query, timeout=5000)
button_element.scroll_into_view_if_needed(timeout=5000)

# we need to retrieve the boundries of the button, the extract the coords and dimentions
bounding_box = button_element.bounding_box()
x, y = bounding_box['x'], bounding_box['y']
width, height = bounding_box['width'], bounding_box['height']

# Click non stop for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    page.mouse.dblclick(x + width/2, y + height /2) # location provided to do the clicking

# To view the test after its finished we use the input function
input('Pausing')

# # If you want to press a mouse key down for x amount of seconds
# # Press the mouse button donw
# page.mouse.down()

# # hold for 4 seconds
# time.sleep(4)

# # Release the mouse button
# page.mouse.up()

page.close()
browser.close()
playwright.stop()
