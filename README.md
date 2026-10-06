# Playwright Python Capstone

## About the Project

This is my Playwright Python capstone project. I built the project to practice UI automation, API testing, pytest, Page Object Model, test data, logging, reporting, and GitHub Actions.

The main UI application used is SauceDemo and the API tests use JSONPlaceholder.

## Tools Used

- Python
- Playwright
- Pytest
- pytest-html
- Git / GitHub
- GitHub Actions

## Project Structure

```text
playwright_capstone/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   └── registration_page.py
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_windows.py
│   │   └── test_session_storage.py
│   └── api/
│       └── test_api.py
├── testdata/
│   ├── login_data.json
│   └── session_data.json
├── utils/
│   ├── api_models.py
│   ├── json_utils.py
│   ├── session_storage.py
│   └── logger.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Applications

UI:
https://www.saucedemo.com/

API:
https://jsonplaceholder.typicode.com/

## Setup

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the packages:

```bash
pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
playwright install chromium
```

## Running Tests

Run all tests:

```bash
pytest
```

Run UI tests:

```bash
pytest tests/ui
```

Run API tests:

```bash
pytest tests/api
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Run readonly tests:

```bash
pytest -m readonly
```

Parallel execution can be run with:

```bash
pytest -n 4
```

## UI Tests

The UI tests cover the main SauceDemo scenarios:

- Valid login
- Invalid login
- Products page
- Add product to cart
- Remove product
- Product details
- Product sorting
- Checkout

I used Playwright locators such as `get_by_role()`, `get_by_text()`, `get_by_label()` and `locator()`.

## Page Object Model

The page classes are inside the `pages` folder.

For example, `LoginPage` contains the login locators and the login method. This keeps the test files focused more on the actual test scenario.

## Data Driven Testing

The login data is stored in:

```text
testdata/login_data.json
```

The test uses `json.load()` and `pytest.mark.parametrize` to run the login test with different data.

## Fixtures and Markers

The reusable pytest fixtures are in `conftest.py`.

The project has these markers:

- `smoke`
- `regression`
- `readonly`

The API request fixture uses `yield` and disposes the request context after the test.

## Multiple Windows

`tests/ui/test_windows.py` demonstrates opening a second browser page and checking the content on the new page.

It uses Playwright's:

```python
browser_page.context.expect_page()
```

## Wait Handling

The project uses Playwright waiting methods such as:

```python
wait_for_url()
wait_for_load_state()
wait_for()
```

These are used instead of adding fixed sleep statements.

## API Tests

The API tests use JSONPlaceholder and cover:

- GET
- POST
- PUT
- DELETE

The tests also check response status and response data.

## API Response Model

`utils/api_models.py` contains the `UserResponse` class.

It is used to access fields from a user response such as:

- id
- name
- username
- email

## Search Without Index

The API test searches the returned users by name instead of assuming a particular array index.

## Deep JSON Comparison

`utils/json_utils.py` contains a recursive function for comparing JSON data.

It can report the location of a mismatch, for example:

```text
root.address.city
```

The project also includes a normal exact comparison using:

```python
assert actual == expected
```

## Session Storage

The session storage functions are in:

```text
utils/session_storage.py
```

The project demonstrates writing, reading, saving, clearing, restoring and validating session storage.

The saved test data is in:

```text
testdata/session_data.json
```

## Logging

Logging is configured in:

```text
utils/logger.py
```

The log file is:

```text
logs/automation.log
```

Important test events are logged without logging passwords.

## Failure Artifacts

The Playwright settings in `pytest.ini` are configured for:

- Trace on failure
- Screenshot on failure
- Video on failure

These can be used to investigate a failed test.

## HTML Report

The project uses `pytest-html`.

Running the tests creates:

```text
report.html
```

The report is configured as a self-contained HTML report.

## GitHub Actions

The workflow is located at:

```text
.github/workflows/playwright.yml
```

It runs for:

- push to `main`
- pull requests to `main`
- manual workflow dispatch

The workflow installs Python and the project dependencies, installs Chromium, runs pytest, and uploads the HTML report.

A successful GitHub Actions run has been completed for the current project.

The HTML report is uploaded as a workflow artifact.

## GitHub Repository

https://github.com/dtripathi25/playwright_capstone

## Current Status

The main framework and CI requirements are working.

The email notification part of the assignment is not configured in this version.
