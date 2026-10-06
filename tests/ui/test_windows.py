def test_multiple_windows(browser_page):
    browser_page.set_content("""
        <button onclick="window.open('', '_blank')">
            Open New Window
        </button>
    """)

    with browser_page.context.expect_page() as new_page_info:
        browser_page.get_by_role(
            "button",
            name="Open New Window"
        ).click()

    new_page = new_page_info.value

    new_page.set_content("<h1>New Window</h1>")

    assert len(browser_page.context.pages) == 2
    assert new_page.get_by_text("New Window").is_visible()