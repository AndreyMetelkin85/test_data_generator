import random
from faker import Faker


def user_data(domain: str = None, locale: str = "en_US"):
    """
        Функция для генерации случайных пользовательских данных:
        имени, фамилии и email-адреса.

        :param domain: Домен почты (например, "gmail.com"). Если не указан, выбирается случайный.
        :param locale: Локаль для генерации имени и фамилии (по умолчанию "en_US").
                       Доступные локали: ["ru_RU", "en_US", "fr_FR", "de_DE"].
        :return: tuple (email, имя, фамилия).
    """

    list_locales = ["ru_RU", "en_US", "fr_FR", "de_DE"]

    if locale is None:
        locale = random.choice(list_locales)
    elif locale not in list_locales:
        raise ValueError(f"Некорректное значение локали: {locale}. Доступные локали: {list_locales}")

    f = Faker(locale=locale)

    first_name = f.first_name()
    last_name = f.last_name()

    available_domains = ["gmail.com", "yahoo.com", "mail.ru", "test.ru"]

    if domain is None:
        domain = random.choice(available_domains)
    elif domain not in available_domains:
        raise ValueError(f"Некорректное значение домена: {domain}. Доступные домены: {available_domains}")

    email = f"{first_name.lower()}_{last_name.lower()}@{domain}"

    return email, first_name, last_name
