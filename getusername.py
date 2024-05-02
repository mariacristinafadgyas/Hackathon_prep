def get_username():
    return input("Enter your username: ")

def test_get_username():
    assert get_username() == "expected_username", "Test failed!"

if __name__ == "__main__":
    test_get_username()
