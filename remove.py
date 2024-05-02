def remove_special_characters(username):
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    cleaned_username = ''.join(char for char in username if char in allowed_characters)
    return cleaned_username

def test_remove_special_characters():
    assert remove_special_characters("user&123_ @") == "user123_", "Test failed!"

if __name__ == "__main__":
    test_remove_special_characters()

