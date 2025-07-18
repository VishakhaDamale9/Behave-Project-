Feature: Validate To-Do List Web Content
  Scenario: Verify the page title
    Given I access the to-do list page
    Then the page title should be "To-Do List"

  Scenario: Verify a task appears in the list
    Given I access the to-do list page
    When I add a task "Buy milk"
    Then the task "Buy milk" should be in the task list