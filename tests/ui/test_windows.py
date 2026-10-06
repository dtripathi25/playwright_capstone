def test_multiple_windows(browser_page):
    browser_page.goto(
    "https://the-internet.herokuapp.com/windows",
    wait_until="commit"
)

    with browser_page.context.expect_page() as new_page_info:
        browser_page.evaluate(
        "window.open('/windows/new', '_blank')"
    )

    new_page = new_page_info.value

    assert len(browser_page.context.pages) == 2
    assert "windows" in browser_page.url
    assert "new" in new_page.url
    assert new_page.get_by_text("New Window").is_visible()