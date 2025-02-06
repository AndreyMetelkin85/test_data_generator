import random

from faker import Faker


def generate_email(domain: str = None, locale: str = "en_US"):
    """ generate mail for a user with different domains """

    list_locals = ["ru_RU", "en_US", "fr_FR", "de_DE"]

    if locale not in list_locals:
        raise ValueError(f'invalid local name: {locale}, valid local name: {list_locals}')
    elif locale is None:
        locale = random.choice(list_locals)

    f = Faker(locale=locale)

    first_name = f.first_name()
    last_name = f.last_name()
    available_domains = ["gmail.com", "yahoo.com", "mail.ru", "test.ru"]

    if domain is None:
        domain = random.choice(available_domains)
    elif domain not in available_domains:
        raise ValueError(f'invalid domain name format: {domain}, valid domain list: {available_domains}')

    return f'{first_name.lower()}_{last_name.lower()}@{domain}'
