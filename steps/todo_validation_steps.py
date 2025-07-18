
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import requests
from bs4 import BeautifulSoup

@given('I access the to-do list page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    for i in range(10):
        try:
            context.driver.get('http://127.0.0.1:5000')
            break
        except WebDriverException:
            time.sleep(0.5)
    else:
        raise Exception("Could not connect to the Flask app at http://127.0.0.1:5000")
    # Fetch page content for BeautifulSoup
    context.page_source = context.driver.page_source
    context.soup = BeautifulSoup(context.page_source, 'lxml')
@then('the page title should be "{expected_title}"')
def step_impl(context, expected_title):
    title = context.soup.find('title').text
    assert title == expected_title, f"Expected title '{expected_title}', got '{title}'"
    context.driver.quit()


@then('the task "{task}" should be in the task list')
def step_impl(context, task):
    task_list = context.soup.find('ul', id='task_list').text
    assert task in task_list, f"Task '{task}' not found in task list"
    context.driver.quit()