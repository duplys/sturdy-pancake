# Test-Driven Development (TDD)

Brief summary and example illustrating **Test-Driven Development**

## TDD Principles

* Develop software driven by tests &ndash; start to program by writing tests!
* What set of tests, when passed, will demonstrate that our code correctly performs the task it was written for?
* Red/Green/Refactor (TDD mantra)
    * 🔴 Write a failing test before you write code
    * 🟢 Make the smallest change possible to make the test pass
    * 🛠️ Refactor to eliminate duplication (and any other technical debt)
* Test infected (phrase that Erich Gamma coined to describe the shift to TDD)
* Start simply -- write automated tests -- refactor to improve (or add) one thing at a time
* Keep it simple, stupid (KISS)
    * Make a todo list to remind you what needs to be done
    * Pick an item and write a test for it
    * Add things to your todo as you go (e.g., things to eliminate technical debts)
    * Red/Green/Refactor
    * Pick next item from the list
* Unit tests and [unit testing frameworks](https://realpython.com/python-testing/) (e.g., `unittest`, `nose`, `pytest`)
    * Tests need to be small
    * Tests need to run fast
    * Convenient "shortcuts" like fixtures and mock-ups
* Unit test vs integration test vs system test vs acceptance test
    * Unit test = test a "unit", typically a function
    * Integration test = tests whether multiple components work in combination
    * System test = test whether the entire system solves some specific tasks
    * Acceptance test = tests whether the software meets end user's expectations
* Grow software organically
* Unit tests are requirements-as-code (specification-as-code)
* Unit tests build a safety net
* Unit tests document the code (especially handy if you have to work with or refactor legacy code)

## Example: Simple Warehouse Management System

The software shall fulfill the following requirements:
* ~~As a user, I want to be able to keep track of items in the warehouse~~
* ~~As a user, I need a method to set the stock~~
* ~~As a user, I want to be able to add items to the warehouse~~
* As a user, I want to be able to remove items from the warehouse
* As a user, I want to be able to get an overview of what's in stock

