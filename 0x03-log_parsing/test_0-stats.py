def test_update_status():
    # Test case 1: Existing status code
    count = {200: 3, 404: 2, 500: 1}
    code = 200
    update_status(code)
    assert count[code] == 4

    # Test case 2: Non-existing status code
    count = {200: 3, 404: 2, 500: 1}
    code = 400
    update_status(code)
    assert count[code] == 1

    # Test case 3: Empty count dictionary
    count = {}
    code = 200
    update_status(code)
    assert count[code] == 1

    # Test case 4: Multiple status codes
    count = {200: 3, 404: 2, 500: 1}
    code = 404
    update_status(code)
    assert count[code] == 3

    # Test case 5: Negative status code
    count = {200: 3, 404: 2, 500: 1}
    code = -200
    update_status(code)
    assert count[code] == 1

test_update_status()