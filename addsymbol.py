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