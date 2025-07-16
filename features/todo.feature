Feature: To-Do List Management
  Scenario: Add a task to the to-do list
    Given I am on the to-do list page
    When I add a task "Buy groceries"
    Then the task "Buy groceries" should appear in the list