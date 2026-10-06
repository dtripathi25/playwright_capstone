def compare_json(actual, expected, path="root"):
    if type(actual) != type(expected):
        return f"{path}: type mismatch"

    if isinstance(actual, dict):
        for key in expected:
            if key not in actual:
                return f"{path}.{key}: missing key"

            result = compare_json(
                actual[key],
                expected[key],
                f"{path}.{key}"
            )

            if result:
                return result

        for key in actual:
            if key not in expected:
                return f"{path}.{key}: unexpected key"

        return None

    if isinstance(actual, list):
        if len(actual) != len(expected):
            return f"{path}: list length mismatch"

        for index, value in enumerate(expected):
            result = compare_json(
                actual[index],
                value,
                f"{path}[{index}]"
            )

            if result:
                return result

        return None

    if actual != expected:
        return f"{path}: expected {expected}, got {actual}"

    return None