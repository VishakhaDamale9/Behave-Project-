from behave import given, when, then
# Import Selenium WebDriver for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Import exception to handle browser connection issues
from selenium.common.exceptions import WebDriverException


@given('I am on the to-do list page')
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

@when('I add a task "{task}"')
def step_impl(context, task):
    # Enter the task into the input field
    context.driver.find_element(By.ID, 'task_input').send_keys(task)
    # Click the add button to submit the task
    context.driver.find_element(By.ID, 'add_button').click()

@then('the task "{task}" should appear in the list')
def step_impl(context, task):
    # Get the text of the task list
    task_list = context.driver.find_element(By.ID, 'task_list').text
    # Assert that the new task appears in the list
    assert task in task_list, f"Task '{task}' not found in list"
    # Close the browser after the check
    context.driver.quit()


