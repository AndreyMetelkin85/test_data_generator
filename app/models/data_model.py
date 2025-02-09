from enum import Enum

class Locale(str, Enum):
    ru_RU = "ru_RU"
    en_US = "en_US"
    fr_FR = "fr_FR"
    de_DE = "de_DE"

class Domain(str, Enum):
    GMAIL = "gmail.com"
    YAHOO = "yahoo.com"
    MAIL_RU = "mail.ru"
    TEST_RU = "test.ru"

class Gender(str, Enum):
    M = "M"
    F = "F"
    X = "X"
