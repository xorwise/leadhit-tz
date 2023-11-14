from fastapi import HTTPException
from tinydb import TinyDB, Query
import re

# Регулярное выражения для даты в формате DD.MM.YYYY
date_regex1 = r"(?:\d{2}\.\d{2}\.\d{4})"

# Регулярное выражение для даты в формате YYYY-MM-DD
date_regex2 = r"(?:\d{4}-\d{2}-\d{2})"

# Регулярное выражения для номера телефона в формате +7 900 999 99 99
phone_regex = r"^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$"

# Регулярное выражение для почты.
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


def find_form(data: dict[str, str], db: TinyDB) -> str:
    """Функция для поиска подходящих шаблонов.
    Возвращает строку - название найденного шаблона, если таких шаблонов нет,
    то выбрасывает исключение.
    """
    templates = list()
    for key in data.keys():
        templates = db.search(Query()[key].exists())
        if len(templates) > 0:
            break

    for template in templates:
        b = True
        for key in template.keys():
            if key == "name":
                continue
            if key not in data:
                b = False
                break
            elif not is_valid_item(data[key], template[key]):
                print("sosok")
                b = False
                break
        if b:
            return template["name"]
    raise HTTPException(404)


def is_valid_item(inp: str, data_type: str) -> bool:
    """Функция для проверки данных на соответствие типу"""
    match data_type:
        case "date":
            return (
                re.match(date_regex1, inp) or re.match(date_regex2, inp)
            ) is not None
        case "phone":
            return re.match(phone_regex, inp) is not None
        case "email":
            return re.match(email_regex, inp) is not None
        case _:
            return type(inp) is str


def create_template(data: dict) -> dict:
    """Функция для создания нового шаблона по
    названиям ключей и типам значений"""
    new_data = dict()
    for key, value in data.items():
        if re.match(date_regex1, value) or re.match(date_regex2, value):
            new_data[key] = "date"
        elif re.match(phone_regex, value):
            new_data[key] = "phone"
        elif re.match(email_regex, value):
            new_data[key] = "email"
        else:
            if type(value) is not str:
                raise HTTPException(422, "Не валидные данные")
            new_data[key] = "text"
    return new_data
