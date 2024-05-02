# python3 main.py
def get_username():
    """Prompt user for username and return the string."""
    return input("Enter your username: ")

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

def add_at_symbol_to_username(username):
    """
    Takes username as an argument, adds the '@' symbol along with an email domain
    to the username, and returns the updated username.
    Example: if the username is 'user123',
             the function should return 'user123@email.com'
    """
    return f"{username}@email.com"

username = get_username()
clean_username = remove_special_characters(username)
email = add_at_symbol_to_username(clean_username)
print("Your email is:", email)
