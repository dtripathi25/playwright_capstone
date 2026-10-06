from pathlib import Path

from utils.session_storage import (
    clear_session_storage,
    read_session_value,
    restore_session_storage,
    save_session_storage,
    validate_session_value,
    write_session_value,
)


def test_session_storage(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    write_session_value(browser_page, "test_user", "Devesh")

    assert read_session_value(browser_page, "test_user") == "Devesh"

    session_file = Path("testdata/session_data.json")
    save_session_storage(browser_page, session_file)

    clear_session_storage(browser_page)
    assert read_session_value(browser_page, "test_user") is None

    restore_session_storage(browser_page, session_file)

    validate_session_value(
        browser_page,
        "test_user",
        "Devesh"
    )