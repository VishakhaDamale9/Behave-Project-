
from behave import given, when, then
# Import Selenium WebDriver and related modules for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
# Import requests and BeautifulSoup for HTML parsing
import requests
from bs4 import BeautifulSoup

@given('I access the to-do list page')
def step_impl(context):
    # Start a new Chrome browser session
    context.driver = webdriver.Chrome()
    # Retry connecting to the Flask server for up to 5 seconds
    for i in range(10):
        try:
            # Attempt to open the to-do list web page
            context.driver.get('http://127.0.0.1:5000')
            break
        except WebDriverException:
            # Wait before retrying if connection fails
            time.sleep(0.5)
    else:
        # Raise an error if unable to connect after retries
        raise Exception("Could not connect to the Flask app at http://127.0.0.1:5000")
    # Fetch page content for BeautifulSoup
    context.page_source = context.driver.page_source
    # Parse the page source with BeautifulSoup for validation steps
    context.soup = BeautifulSoup(context.page_source, 'lxml')
@then('the page title should be "{expected_title}"')
def step_impl(context, expected_title):
    # Find the <title> tag in the HTML and check its text
    title = context.soup.find('title').text
    assert title == expected_title, f"Expected title '{expected_title}', got '{title}'"
    # Close the browser after the check
    context.driver.quit()


@then('the task "{task}" should be in the task list')
def step_impl(context, task):
    # Get the text of the task list and check if the task is present
    task_list = context.soup.find('ul', id='task_list').text
    assert task in task_list, f"Task '{task}' not found in task list"
    # Close the browser after the check
    context.driver.quit()