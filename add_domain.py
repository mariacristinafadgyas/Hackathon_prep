def add_domain_to_username(username):
    """ takes username as an argument and adds
    a domain name symbol to the username and return the email
    Example: if the username is user123@
             the function should return user123@email.com
    """
    username = username + "email.com"
    return username


def main():
    username = add_domain_to_username("doe@")
    assert username == "doe@email.com"

if __name__ == "__main__":
    main()

