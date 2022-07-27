''' Just a simple example of playwright tests.
To run: pytest [--headed] test.py'''
from playwright.sync_api import Page
import pytest

GREETINGS_TEXT='id=nav-link-accountList-nav-line-1'
SEARCH_BAR='id=twotabsearchtextbox'
SEARCH_BUTTON='id=nav-search-submit-text'
TITLE='.a-spacing-base'

def test_website_is_opening(page: Page):
    response = page.goto("https://amazon.com")
    assert response.ok, 'The website does not reply with 2xx'

    actual_text = page.locator(GREETINGS_TEXT).inner_text()
    expected_text = 'Hello, Sign in'
    assert actual_text == expected_text, f'Received: {actual_text}'


def test_search_results(page: Page):
    page.goto("https://amazon.com")
    page.locator(SEARCH_BAR).fill('book')
    page.locator(SEARCH_BUTTON).click()

    actual_title = page.locator(TITLE).inner_text()
    expected_title = 'Best sellers'
    assert actual_title == expected_title, f'Received: {actual_title}'