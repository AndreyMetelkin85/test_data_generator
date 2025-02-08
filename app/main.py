from typing import Optional
import uvicorn
from fastapi import FastAPI, Query, HTTPException
from app.models.data_model import Locale, Domain
from app.services.data_service import user_data, password, profile

app = FastAPI()


@app.get(path="/user_data",
         tags=["User data"],
         description="Эндпоинт генерирует случайные данные пользователя, включая имя, фамилию, email-адрес, а так же"
                     "мобильный номер телефона. Локализация влияет на формат имени и фамилии, номера телефона,"
                     "а домен — на email.",
         response_description="Возвращает JSON с именем, фамилией, мобильным номером и email-адресом",
         responses={
             200: {
                 "description": "Успешный ответ с сгенерированными данными",
                 "content": {
                     "application/json": {
                         "example": {
                             "first_name": "Иван",
                             "last_name": "Петров",
                             "email": "ivan_petrov@mail.ru",
                             "mobile_phone": +79031234567
                         }
                     }
                 }
             },
             400: {
                 "description": "Некорректные параметры (например, неверная локализация или домен)"
             }
         }
         )
def generate_user_data_endpoint(
        locale: Optional[Locale] = Query(default=None, description="Локализация:"),
        domain: Optional[Domain] = Query(default=None, description="Домен для email:")
):
    try:
        locale_value = locale.value if locale else None
        domain_value = domain.value if domain else None

        email, first_name, last_name, mobile_phone = user_data(domain=domain_value, locale=locale_value)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "mobile_phone": mobile_phone
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    path="/generate_password",
    tags=["Password"],
    description=(
            "Генерирует безопасный пароль с заданными параметрами. "
            "Вы можете указать длину пароля, а также выбрать, "
            "должны ли в нем присутствовать цифры, спецсимволы, "
            "заглавные и строчные буквы."
    ),
    response_description="Возвращает сгенерированный пароль в JSON-формате",
    responses={
        200: {
            "description": "Успешный ответ с сгенерированным паролем",
            "content": {
                "application/json": {
                    "example": {"password": "A2b#7dX@z"}
                }
            },
        },
        400: {
            "description": "Некорректные параметры (например, длина вне диапазона 6-50 символов)"
        },
    }
)
def generate_password_user_endpoint(
        password_length: Optional[int] = Query(default=6, description="Длина пароля", ge=6, le=50),
        special_chars: Optional[bool] = Query(default=False, description="Добавить спецсимволы"),
        digits: Optional[bool] = Query(default=False, description="Добавить цифры"),
        upper_case: Optional[bool] = Query(default=False, description="Добавить заглавные буквы"),
        lower_case: Optional[bool] = Query(default=True, description="Добавить строчные буквы")
):
    try:
        generate_password = password(length=password_length,
                                     special_chars=special_chars,
                                     digits=digits,
                                     upper_case=upper_case,
                                     lower_case=lower_case)
        return {"password": generate_password}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(path="/profile_data",
         tags=["User data"])
def generate_profile_endpoint(
        locale: Optional[Locale] = Query(default=None, description="Локализация")
):
    profiles = profile(locale=locale)

    return {"profile": profiles}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
