import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def browser_page(page: Page):
    yield page


@pytest.fixture
def api_request_context(playwright: Playwright):
    request = playwright.request.new_context()
    yield request
    request.dispose()