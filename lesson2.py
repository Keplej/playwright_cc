import time
from playwright.sync_api import sync_playwright

# In this lesson we will learn how to interact with page elements like input fields, dropdowns, checkboxes, scrollbars, buttons

# To save the page as an html file:
def save_page_html(page, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page.content())
        print(f'Page HTML saved to {filename}')
    except Exception as e:
        print(f'Error saving page HTML to {filename}: {e}')


URL = 'https://minneapolis.craigslist.org/'
xpath_prefix = 'xpath='

# This is to launch a playwright session
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)

page = browser.new_page(java_script_enabled=True)
page.goto(URL, wait_until='load')

time.sleep(2)

# create input element reference
xpath_input = '//input[@placeholder="search craigslist"]'
page.wait_for_selector(xpath_prefix + xpath_input, timeout=5000)
input_element = page.query_selector(xpath_prefix + xpath_input)

# if the input_element is not found by the xpath query we provided the input element will return nothing.
# In that case we cna use an if statement to say if input element is created, we can search using the fill method and press enter.
# We wait for the page to load ensures the result page is loaded first before we move on to the next action
if input_element:
    # fill in the search term and press enter
    input_element.fill('apartment')
    input_element.press('Enter')

    # wait for the page to load
    page.wait_for_load_state('domcontentloaded')

    # Locate the panel element
    xpath_search_panel = '//div[@class="cl-search-filters-panel"]'
    page.wait_for_selector(xpath_prefix + xpath_search_panel, timeout=7000)
    search_panel = page.locator(xpath_prefix + xpath_search_panel) # locator allows us to work with dynamic elements
    # locator allows us to work with dynamic elements with features like: 
    # auto-weighting, multi-element handles, and element reattachment versus querySelector is a lower level method to work with the first element it finds.

    # Checking if the panel element is found 
    if search_panel.count() > 0:
        xpath_checkbox = '//input[@type="checkbox" and @name="postedToday"]'

        # Wait for the checkbox to be visible
        page.wait_for_selector(xpath_prefix + xpath_checkbox, state='visible')

        checkbox_element = page.locator(xpath_prefix + xpath_checkbox)

        # To toggle a checkbox
        if checkbox_element.count() > 0:
            # Toggle
            if checkbox_element.is_checked():
                checkbox_element.uncheck()
            else:
                checkbox_element.check()
            
            page.wait_for_load_state('domcontentloaded')
        
        # Reattach the search_panel element
        search_panel = search_panel.element_handle()

        # Scroll to the bottom of the panel element
        page.evaluate('element => element.scrollTop = element.scrollHeight', search_panel)

        # Select an option from a drop-down
        xpath_dropdown = '//select[@name="availabilityMode"]'
        dropdown_element = search_panel.query_selector(xpath_prefix + xpath_dropdown)
        
        if dropdown_element:
            # select_option you can use whatever method based on preference
            # dropdown_element.select_option('1') select based on the index (2nd item)
            dropdown_element.select_option(label='within 30 days') # this is picking what you want to select on the dropdown

        # Click the apply button
        xpath_button = '//button[@type="button" and contains(@class, "cl-exec-search")]'
        button_element = search_panel.query_selector(xpath_prefix + xpath_button)

        if button_element:
            button_element.click()

        page.wait_for_load_state('domcontentloaded')

        # click on first result
        xpath_first_result = '(//a[@class="main"])'
        page.wait_for_selector(xpath_prefix + xpath_first_result, timeout=5000)
        first_result = page.query_selector(xpath_prefix + xpath_first_result)
        
        if first_result:
            first_result.click()
        
        page.wait_for_load_state('load')

        time.sleep(1)

        # Save page HTML to file
        save_page_html(page, 'html-export/first-result.html')


page.close()
browser.close()
playwright.stop()
