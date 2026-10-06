import json


def write_session_value(page, key, value):
    page.evaluate(
        """([key, value]) => sessionStorage.setItem(key, value)""",
        [key, value]
    )


def read_session_value(page, key):
    return page.evaluate(
        """key => sessionStorage.getItem(key)""",
        key
    )


def save_session_storage(page, file_path):
    session_data = page.evaluate(
        """() => Object.fromEntries(Object.entries(sessionStorage))"""
    )

    with open(file_path, "w") as file:
        json.dump(session_data, file, indent=4)


def clear_session_storage(page):
    page.evaluate("sessionStorage.clear()")


def restore_session_storage(page, file_path):
    with open(file_path) as file:
        session_data = json.load(file)

    for key, value in session_data.items():
        write_session_value(page, key, value)


def validate_session_value(page, key, expected_value):
    actual_value = read_session_value(page, key)
    assert actual_value == expected_value