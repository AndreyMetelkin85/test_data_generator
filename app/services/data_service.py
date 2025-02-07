import random
from faker import Faker


def user_data(domain: str = None, locale: str = "en_US"):
    """
        Функция для генерации случайных пользовательских данных:
        имени, фамилии, email-адреса и номера мобильного телефона.

        :param domain: Домен почты (например, "gmail.com").
                       Если не указан, выбирается случайный из доступных.
        :param locale: Локаль для генерации имени, фамилии и номера телефона (по умолчанию "en_US").
                       Доступные локали: ["ru_RU", "en_US", "fr_FR", "de_DE"].
        :return: tuple (email, имя, фамилия, номер телефона).

        Логика генерации телефонных номеров:
        - "ru_RU" (Россия): формат +7 XXX XXXXXXX (код оператора + 7 цифр)
        - "en_US" (США): формат +1 XXX XXXXXXX (код оператора + 7 цифр)
        - "fr_FR" (Франция): формат +33 X XXXXXXXX (код оператора + 8 цифр)
        - "de_DE" (Германия): формат +49 XXX XXXXXXX (код оператора + 7 цифр)

        Доступные домены для email: ["gmail.com", "yahoo.com", "mail.ru", "test.ru"].
    """

    list_locales = ["ru_RU", "en_US", "fr_FR", "de_DE"]

    if locale is None:
        locale = random.choice(list_locales)
    elif locale not in list_locales:
        raise ValueError(f"Некорректное значение локали: {locale}. Доступные локали: {list_locales}")

    f = Faker(locale=locale)

    first_name = f.first_name()
    last_name = f.last_name()

    # Работа с телефонными номерами
    mobile_phone = ""
    if locale == list_locales[0]:  # Россия
        operator_mobile_code = random.choice([903, 915, 926, 917, 901, 925, 999])
        phone_number = "".join(str(random.randint(0, 9)) for _ in range(7))
        mobile_phone = f'+7{operator_mobile_code}{phone_number}'

    elif locale == list_locales[1]:  # США
        operator_mobile_code = random.choice([212, 310, 786, 661, 818, 424, 929])
        phone_number = "".join(str(random.randint(0, 9)) for _ in range(10))
        mobile_phone = f'+1{operator_mobile_code}{phone_number}'

    elif locale == list_locales[2]:  # Франция
        operator_mobile_code = random.choice([6, 7])
        phone_number = "".join(str(random.randint(0, 9)) for _ in range(8))
        mobile_phone = f'+33{operator_mobile_code}{phone_number}'

    elif locale == list_locales[3]:  # Германия
        operator_mobile_code = random.choice([151, 152, 160, 170, 175, 176])
        phone_number = "".join(str(random.randint(0, 9)) for _ in range(7))
        mobile_phone = f'+49{operator_mobile_code}{phone_number}'

    available_domains = ["gmail.com", "yahoo.com", "mail.ru", "test.ru"]

    if domain is None:
        domain = random.choice(available_domains)
    elif domain not in available_domains:
        raise ValueError(f"Некорректное значение домена: {domain}. Доступные домены: {available_domains}")

    email = f"{first_name.lower()}_{last_name.lower()}@{domain}"

    return email, first_name, last_name, mobile_phone


def password(length: int, special_chars: bool, digits: bool, upper_case: bool, lower_case: bool) -> str:
    f = Faker(locale="en_US")

    generate_password = f.password(length=length,
                                   special_chars=special_chars,
                                   digits=digits,
                                   upper_case=upper_case,
                                   lower_case=lower_case
                                   )
    return generate_password
