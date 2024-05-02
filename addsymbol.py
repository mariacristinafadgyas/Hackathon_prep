def add_at_symbol_to_username(username):
    return f"{username}@email.com"

def test_add_at_symbol_to_username():
    assert add_at_symbol_to_username("user123_") == "user123_@email.com", "Test failed!"

if __name__ == "__main__":
    test_add_at_symbol_to_username()
