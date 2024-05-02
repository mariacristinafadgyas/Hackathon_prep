# from getusername import get_username
# from remove import remove_special_characters
# from addsymbol import add_at_symbol_to_username
# from add_domain import add_domain_to_username
# from display_email import display_email_address

import getusername
import remove
import addsymbol
import add_domain
import display_email


def main():
    user_name = getusername.get_username()
    cleaned_username = remove.remove_special_characters(user_name)
    user_name_at = addsymbol.add_at_symbol_to_username(cleaned_username)
    final_user_name = add_domain.add_domain_to_username(user_name_at)
    display_email.display_email_address(final_user_name)


if __name__ == "__main__":
    main()



