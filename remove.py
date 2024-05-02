def remove_special_characters(username):
    """
    Takes username as an argument, removes all special characters
    except underscores, and returns the updated username.
    Example: if the username is 'user&123_ @',
             the function should return 'user123_'
    """
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    cleaned_username = ''.join(char for char in username if char in allowed_characters)
    return cleaned_username
